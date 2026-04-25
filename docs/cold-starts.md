# Cold starts, scale-to-zero, and auto-wake

This is the most surprising thing about running custom models on
Graphn the first time. Read this once and you'll never get bitten.

## What's happening under the hood

Graphn deploys every custom model as a KServe `InferenceService`
backed by a Kubernetes deployment. By default, custom models are
**scaled to zero** when idle:

```
min_replicas:        0
max_replicas:        1
cooldown_seconds:    600
```

That means: ten minutes after your last request, the gateway
descheduled your pod, and your `replicas_available` dropped from
`1` to `0`. The next request has to wait while:

1. The gateway scales the deployment from `0 → 1` desired replicas.
2. Kubernetes schedules a pod onto a GPU node.
3. The pod pulls the model image (cached, usually fast).
4. The model loads weights into GPU memory.
5. The serving runtime warms up.

End-to-end this typically takes **60s – 600s** depending on weight
size, GPU availability, and image cache state.

## What you'll see without auto-wake

Without help, the first request after the cooldown returns:

```
HTTP/1.1 503 Service Unavailable
Content-Type: application/json

{
  "error": {
    "message": "Model is scaled to zero and is now warming up. Try again in 1-2 minutes.",
    "type": "service_unavailable"
  }
}
```

This is the gateway being honest: it has correctly identified that
you want this model, kicked off the warm-up, and told you to come
back. But "come back" is a lot of bookkeeping for the caller.

## What auto-wake does

When you call `client.chat.completions.create(model="custom:cm_...", ...)`
and the gateway returns one of those cold-start 503s, the SDK
transparently:

1. Calls `POST /v1/{workspace}/custom-models/{cm_id}/wake` to nudge
   the autoscaler explicitly. This is idempotent — safe to call when
   the model is already up.
2. Sleeps with exponential backoff (2s → 15s).
3. Retries the chat completion.
4. Repeats until the gateway returns 2xx, the error is no longer a
   cold-start error, or `wake_timeout` (default 180 seconds)
   elapses.

If the timeout is hit, the original 503 is re-raised so you can
handle it however you'd handle any other API error.

```python
import graphn

with graphn.Client() as c:
    resp = c.chat.completions.create(
        model=model.qualified_name,
        messages=[{"role": "user", "content": "hi"}],
        wake_timeout=600,  # give it up to 10 min of warm-up
    )
```

## The knobs

| Parameter | Default | What it does |
|---|---|---|
| `auto_wake` | `True` | If `False`, cold-start 503s pass through unchanged. |
| `wake_timeout` | `180.0` | Seconds to keep retrying before giving up. |

```python
# Default behavior — auto-wake on, 3 minute budget.
c.chat.completions.create(model=..., messages=[...])

# Larger model, longer cold start. Up to 15 minutes.
c.chat.completions.create(model=..., messages=[...], wake_timeout=900)

# I want raw 503s — I have my own retry logic.
c.chat.completions.create(model=..., messages=[...], auto_wake=False)
```

## When auto-wake does NOT fire

By design, auto-wake only triggers for **custom models**. Specifically:

- The model id must be of the form `custom:cm_<hex>` (the canonical
  form returned by `CustomModel.qualified_name`).
- The error must be a 502/503/504 with a body that contains one of:
  `"scaled to zero"`, `"warming up"`, `"not ready"`, or
  `"no available replicas"`.

For built-in or imported (BYO) models, 5xx responses pass through
unchanged because we have no way to wake them.

## Forcing a wake without making a chat request

If you know you're about to issue a burst of traffic and want to
amortize the cold start before the user is waiting:

```python
woken = c.custom_models.wake(model_id)
print(woken.replicas_desired)  # should be > 0 now
```

This returns immediately after the gateway accepts the wake call;
it doesn't wait for the pod to finish loading. To actually block
until the model is serving, the chat call (with `auto_wake=True`)
is the simplest signal — by the time the first 2xx comes back, the
pod is live.

## Avoiding cold starts entirely

If you can afford the GPU-hours, set `min_replicas=1` at create time:

```python
model = c.custom_models.create(
    name="always-warm",
    huggingface_model_id="...",
    weight_source="huggingface",
    min_replicas=1,         # at least one pod always running
    cooldown_seconds=0,     # don't bother with the cooldown timer
)
```

This trades cost for latency. Most users want the default
(scale-to-zero) for dev and a separate `min_replicas=1` deployment
for production.

## What the model status actually means

A subtle thing: `model.status == "ready"` means the deployment exists
and is reconciled, **not** that there is a pod actively serving. With
`min_replicas=0`, a `ready` model will reliably have
`replicas_available=0` until something pokes it.

This is why `wait_until_ready()` returns quickly even on a cold
workspace — it's waiting for the K8s deployment to exist, not for a
pod to be live. The `chat.completions.create` call is what blocks
on the actual cold start, and (with `auto_wake=True`) handles it
for you.
