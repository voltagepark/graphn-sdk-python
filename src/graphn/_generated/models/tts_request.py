from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.tts_request_response_format import TTSRequestResponseFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="TTSRequest")


@_attrs_define
class TTSRequest:
    """
    Attributes:
        model (str): TTS model alias (built-in) or `custom:<id>` / `imported:<id>`.
        text (str): Text to synthesize.
        speaker (str): Voice identifier from `listTtsVoices`.
        lang (str | Unset): ISO-639-1 language code.
        sampling_rate (int | Unset): Output sampling rate in Hz (Rime providers). Default: 24000.
        speed_alpha (float | Unset): Playback speed multiplier (1.0 = normal).
        response_format (TTSRequestResponseFormat | Unset): Output audio format (Qwen providers).
        top_p (float | Unset):
        temperature (float | Unset):
        repetition_penalty (float | Unset):
        max_tokens (int | Unset):
        instructions (str | Unset): Style/instruction prompt (Qwen providers).
    """

    model: str
    text: str
    speaker: str
    lang: str | Unset = UNSET
    sampling_rate: int | Unset = 24000
    speed_alpha: float | Unset = UNSET
    response_format: TTSRequestResponseFormat | Unset = UNSET
    top_p: float | Unset = UNSET
    temperature: float | Unset = UNSET
    repetition_penalty: float | Unset = UNSET
    max_tokens: int | Unset = UNSET
    instructions: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        text = self.text

        speaker = self.speaker

        lang = self.lang

        sampling_rate = self.sampling_rate

        speed_alpha = self.speed_alpha

        response_format: str | Unset = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = self.response_format.value

        top_p = self.top_p

        temperature = self.temperature

        repetition_penalty = self.repetition_penalty

        max_tokens = self.max_tokens

        instructions = self.instructions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model": model,
                "text": text,
                "speaker": speaker,
            }
        )
        if lang is not UNSET:
            field_dict["lang"] = lang
        if sampling_rate is not UNSET:
            field_dict["samplingRate"] = sampling_rate
        if speed_alpha is not UNSET:
            field_dict["speedAlpha"] = speed_alpha
        if response_format is not UNSET:
            field_dict["responseFormat"] = response_format
        if top_p is not UNSET:
            field_dict["topP"] = top_p
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if repetition_penalty is not UNSET:
            field_dict["repetitionPenalty"] = repetition_penalty
        if max_tokens is not UNSET:
            field_dict["maxTokens"] = max_tokens
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        text = d.pop("text")

        speaker = d.pop("speaker")

        lang = d.pop("lang", UNSET)

        sampling_rate = d.pop("samplingRate", UNSET)

        speed_alpha = d.pop("speedAlpha", UNSET)

        _response_format = d.pop("responseFormat", UNSET)
        response_format: TTSRequestResponseFormat | Unset
        if isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = TTSRequestResponseFormat(_response_format)

        top_p = d.pop("topP", UNSET)

        temperature = d.pop("temperature", UNSET)

        repetition_penalty = d.pop("repetitionPenalty", UNSET)

        max_tokens = d.pop("maxTokens", UNSET)

        instructions = d.pop("instructions", UNSET)

        tts_request = cls(
            model=model,
            text=text,
            speaker=speaker,
            lang=lang,
            sampling_rate=sampling_rate,
            speed_alpha=speed_alpha,
            response_format=response_format,
            top_p=top_p,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            max_tokens=max_tokens,
            instructions=instructions,
        )

        return tts_request
