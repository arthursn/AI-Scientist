from fnmatch import fnmatch

SUPPORTED_MODELS = [
    "claude-3-5-sonnet-20240620",
    "gpt-4o-2024-05-13",
    "deepseek-coder-v2-0724",
    "llama3.1-405b",
    # Anthropic Claude models via Amazon Bedrock
    "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
    "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
    "bedrock/anthropic.claude-3-haiku-20240307-v1:0",
    "bedrock/anthropic.claude-3-opus-20240229-v1:0"
    # Anthropic Claude models Vertex AI
    "vertex_ai/claude-3-opus@20240229",
    "vertex_ai/claude-3-5-sonnet@20240620",
    "vertex_ai/claude-3-sonnet@20240229",
    "vertex_ai/claude-3-haiku@20240307",
    # Azure models
    "azure/*",
]


def is_model_supported(model):
    return any(fnmatch(model, supported_model) for supported_model in SUPPORTED_MODELS)
