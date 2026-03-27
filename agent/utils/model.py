import os

from langchain.chat_models import init_chat_model

OPENAI_RESPONSES_WS_BASE_URL = "wss://api.openai.com/v1"


def make_model(model_id: str, **kwargs: dict):
    model_kwargs = kwargs.copy()

    if model_id.startswith("openai:"):
        # 如果设置了 OPENAI_BASE_URL（如 OpenRouter），走标准 REST API
        # 只有直连 OpenAI 时才走 Responses WebSocket API
        custom_base = os.getenv("OPENAI_BASE_URL")
        if custom_base and "openai.com" not in custom_base:
            model_kwargs["base_url"] = custom_base
        else:
            model_kwargs["base_url"] = OPENAI_RESPONSES_WS_BASE_URL
            model_kwargs["use_responses_api"] = True

    return init_chat_model(model=model_id, **model_kwargs)
