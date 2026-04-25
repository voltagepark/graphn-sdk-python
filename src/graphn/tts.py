"""Text-to-speech resource.

Hand-written because the OpenAI SDK's ``audio.speech`` API does not
match Graphn's ``/v1/tts`` request shape (we expose ``speaker``, ``lang``,
``samplingRate``, ``speedAlpha``, ``responseFormat``). The endpoint is
served by the inference host but accepts an ``X-Workspace-Id`` header
in the standard transport, so we route it through the same httpx
machinery as the control-plane resources — just pointed at the
inference host.
"""

from __future__ import annotations

from typing import Any, Literal

import httpx

from graphn._transport import (
    AsyncTransport,
    SyncTransport,
    _build_error,
    _TransportConfig,
)

ResponseFormat = Literal["mp3", "wav", "opus", "flac", "pcm"]
"""Audio container the upstream returns. Maps 1:1 to MIME types."""

_FORMAT_TO_MIME: dict[ResponseFormat, str] = {
    "mp3": "audio/mpeg",
    "wav": "audio/wav",
    "opus": "audio/opus",
    "flac": "audio/flac",
    "pcm": "audio/pcm",
}

_TTS_PATH = "/v1/tts"
_VOICES_PATH = "/v1/tts/voices"


def _build_synth_body(
    *,
    model: str,
    text: str,
    speaker: str,
    lang: str | None,
    sampling_rate: int | None,
    speed_alpha: float | None,
    response_format: ResponseFormat | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"model": model, "text": text, "speaker": speaker}
    if lang is not None:
        body["lang"] = lang
    if sampling_rate is not None:
        body["samplingRate"] = sampling_rate
    if speed_alpha is not None:
        body["speedAlpha"] = speed_alpha
    if response_format is not None:
        body["responseFormat"] = response_format
    return body


def _accept_header(response_format: ResponseFormat | None) -> str:
    if response_format is None:
        return ", ".join(_FORMAT_TO_MIME.values())
    return _FORMAT_TO_MIME[response_format]


def _inference_headers(cfg: _TransportConfig, accept: str) -> dict[str, str]:
    headers = cfg.auth_headers()
    headers["Accept"] = accept
    return headers


class TTS:
    """Synchronous text-to-speech resource."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        # The shared SyncTransport is bound to the control-plane base
        # URL; TTS lives on the inference host, so we keep a dedicated
        # httpx client here. Lazy so customers who never call TTS pay
        # nothing.
        self._client: httpx.Client | None = None

    def _http(self) -> httpx.Client:
        if self._client is None:
            cfg = self._transport.cfg
            self._client = httpx.Client(base_url=cfg.inference_url, timeout=cfg.timeout)
        return self._client

    def synthesize(
        self,
        *,
        model: str,
        text: str,
        speaker: str,
        lang: str | None = None,
        sampling_rate: int | None = None,
        speed_alpha: float | None = None,
        response_format: ResponseFormat | None = None,
    ) -> bytes:
        cfg = self._transport.cfg
        accept = _accept_header(response_format)
        response = self._http().post(
            _TTS_PATH,
            json=_build_synth_body(
                model=model,
                text=text,
                speaker=speaker,
                lang=lang,
                sampling_rate=sampling_rate,
                speed_alpha=speed_alpha,
                response_format=response_format,
            ),
            headers=_inference_headers(cfg, accept),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return response.content

    def voices(self, *, model: str) -> dict[str, Any]:
        cfg = self._transport.cfg
        response = self._http().get(
            _VOICES_PATH,
            params={"model": model},
            headers=_inference_headers(cfg, "application/json"),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return response.json()

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None


class AsyncTTS:
    """Asynchronous text-to-speech resource."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self._client: httpx.AsyncClient | None = None

    def _http(self) -> httpx.AsyncClient:
        if self._client is None:
            cfg = self._transport.cfg
            self._client = httpx.AsyncClient(base_url=cfg.inference_url, timeout=cfg.timeout)
        return self._client

    async def synthesize(
        self,
        *,
        model: str,
        text: str,
        speaker: str,
        lang: str | None = None,
        sampling_rate: int | None = None,
        speed_alpha: float | None = None,
        response_format: ResponseFormat | None = None,
    ) -> bytes:
        cfg = self._transport.cfg
        accept = _accept_header(response_format)
        response = await self._http().post(
            _TTS_PATH,
            json=_build_synth_body(
                model=model,
                text=text,
                speaker=speaker,
                lang=lang,
                sampling_rate=sampling_rate,
                speed_alpha=speed_alpha,
                response_format=response_format,
            ),
            headers=_inference_headers(cfg, accept),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return response.content

    async def voices(self, *, model: str) -> dict[str, Any]:
        cfg = self._transport.cfg
        response = await self._http().get(
            _VOICES_PATH,
            params={"model": model},
            headers=_inference_headers(cfg, "application/json"),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return response.json()

    async def aclose(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None
