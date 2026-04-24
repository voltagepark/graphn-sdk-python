"""Contains all the data models used in inputs/outputs"""

from .architecture_info import ArchitectureInfo
from .capability import Capability
from .chat_completion_request import ChatCompletionRequest
from .chat_completion_request_response_format import ChatCompletionRequestResponseFormat
from .chat_completion_request_tool_choice_type_1 import (
    ChatCompletionRequestToolChoiceType1,
)
from .chat_completion_request_tools_item import ChatCompletionRequestToolsItem
from .chat_completion_response import ChatCompletionResponse
from .chat_completion_response_choices_item import ChatCompletionResponseChoicesItem
from .chat_completion_response_object import ChatCompletionResponseObject
from .chat_completion_response_usage import ChatCompletionResponseUsage
from .chat_message import ChatMessage
from .chat_message_role import ChatMessageRole
from .chat_message_tool_calls_item import ChatMessageToolCallsItem
from .custom_model import CustomModel
from .custom_model_access import CustomModelAccess
from .custom_model_create import CustomModelCreate
from .custom_model_create_quantization import CustomModelCreateQuantization
from .custom_model_list import CustomModelList
from .custom_model_quantization import CustomModelQuantization
from .custom_model_status import CustomModelStatus
from .discover_imported_models_request import DiscoverImportedModelsRequest
from .discover_imported_models_response import DiscoverImportedModelsResponse
from .discovered_imported_model import DiscoveredImportedModel
from .error import Error
from .gpu_hours_response import GpuHoursResponse
from .inference_error import InferenceError
from .inference_error_error import InferenceErrorError
from .list_tts_voices_response_200 import ListTtsVoicesResponse200
from .model import Model
from .model_list import ModelList
from .model_list_object import ModelListObject
from .model_object import ModelObject
from .model_owned_by import ModelOwnedBy
from .secret import Secret
from .secret_create import SecretCreate
from .secret_list import SecretList
from .secret_update import SecretUpdate
from .supported_architectures import SupportedArchitectures
from .test_connection_request import TestConnectionRequest
from .test_connection_response import TestConnectionResponse
from .test_connection_response_usage import TestConnectionResponseUsage
from .tts_request import TTSRequest
from .tts_request_response_format import TTSRequestResponseFormat
from .validate_model_request import ValidateModelRequest
from .validate_model_request_quantization import ValidateModelRequestQuantization
from .validate_model_response import ValidateModelResponse
from .weight_source import WeightSource

__all__ = (
    "ArchitectureInfo",
    "Capability",
    "ChatCompletionRequest",
    "ChatCompletionRequestResponseFormat",
    "ChatCompletionRequestToolChoiceType1",
    "ChatCompletionRequestToolsItem",
    "ChatCompletionResponse",
    "ChatCompletionResponseChoicesItem",
    "ChatCompletionResponseObject",
    "ChatCompletionResponseUsage",
    "ChatMessage",
    "ChatMessageRole",
    "ChatMessageToolCallsItem",
    "CustomModel",
    "CustomModelAccess",
    "CustomModelCreate",
    "CustomModelCreateQuantization",
    "CustomModelList",
    "CustomModelQuantization",
    "CustomModelStatus",
    "DiscoveredImportedModel",
    "DiscoverImportedModelsRequest",
    "DiscoverImportedModelsResponse",
    "Error",
    "GpuHoursResponse",
    "InferenceError",
    "InferenceErrorError",
    "ListTtsVoicesResponse200",
    "Model",
    "ModelList",
    "ModelListObject",
    "ModelObject",
    "ModelOwnedBy",
    "Secret",
    "SecretCreate",
    "SecretList",
    "SecretUpdate",
    "SupportedArchitectures",
    "TestConnectionRequest",
    "TestConnectionResponse",
    "TestConnectionResponseUsage",
    "TTSRequest",
    "TTSRequestResponseFormat",
    "ValidateModelRequest",
    "ValidateModelRequestQuantization",
    "ValidateModelResponse",
    "WeightSource",
)
