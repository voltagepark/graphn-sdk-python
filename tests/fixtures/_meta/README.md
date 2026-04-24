# Canonical fixture payloads

Each subdirectory mirrors an OpenAPI tag. File names follow the pattern:

```
<operationId>.<request|response>[.<status>].<ext>
```

Examples:
- `createCustomModel.request.json` — request body for `POST /v1/{workspaceId}/custom-models`
- `createCustomModel.response.201.json` — successful response body
- `getCustomModel.response.404.json` — error response body
- `chatCompletions.streaming.txt` — raw SSE stream (one event per `data: ...` line)

These fixtures are the **single source of truth** for example payloads:

1. The SDK's tests load them (so realism is enforced — drift breaks tests).
2. The `release-openapi.yml` workflow in `takao` copies this directory verbatim into
   the public `voltagepark/graphn-openapi` repo on each spec release, so customers
   generating clients in TS/Go/Java have ready-made golden payloads to test against.

When you add a new operation to the OpenAPI spec, add a fixture pair here.
When response shapes change, update the fixture **and** bump the spec version.
