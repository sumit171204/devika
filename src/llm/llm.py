<<<<<<< HEAD
from enum import Enum
from typing import List, Tuple
=======
import tiktoken
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d

from src.socket_instance import emit_agent
from .ollama_client import Ollama
from .claude_client import Claude
<<<<<<< HEAD
from .openai_client import OpenAI
from .groq_client import Groq

from src.state import AgentState

import tiktoken
=======
from .openai_client import OpenAi
from .gemini_client import Gemini
from .mistral_client import MistralAi
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d

from ..config import Config
from ..logger import Logger

TOKEN_USAGE = 0
TIKTOKEN_ENC = tiktoken.get_encoding("cl100k_base")

<<<<<<< HEAD
class Model(Enum):
    CLAUDE_3_OPUS = ("Claude 3 Opus", "claude-3-opus-20240229")
    CLAUDE_3_SONNET = ("Claude 3 Sonnet", "claude-3-sonnet-20240229")
    CLAUDE_3_HAIKU = ("Claude 3 Haiku", "claude-3-haiku-20240307")
    GPT_4_TURBO = ("GPT-4 Turbo", "gpt-4-0125-preview")
    GPT_3_5 = ("GPT-3.5", "gpt-3.5-turbo-0125")
    OLLAMA_MODELS = [
        (
            model["name"].split(":")[0],
            model["name"],
        )
        for model in Ollama.list_models()
    ]
    GROQ_MIXTRAL_8X7B_32768 = ("GROQ Mixtral", "mixtral-8x7b-32768")
    GROQ_LLAMA2_70B_4096 = ("GROQ LLAMA2-70B", "llama2-70b-4096")
    GROQ_GEMMA_7B_IT = ("GROQ GEMMA-7B-IT", "gemma-7b-it")


logger = Logger(filename="devika_prompts.log")
=======
ollama = Ollama()

>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d

class LLM:
    def __init__(self, model_id: str = None):
        self.model_id = model_id
<<<<<<< HEAD
        self.log_prompts = Config().get_logging_prompts()
    
    def list_models(self) -> List[Tuple[str, str]]:
        return [model.value for model in Model if model.name != "OLLAMA_MODELS"] + list(
            Model.OLLAMA_MODELS.value
        )
=======
        self.models = {
            "CLAUDE": [
                ("Claude 3 Opus", "claude-3-opus-20240229"),
                ("Claude 3 Sonnet", "claude-3-sonnet-20240229"),
                ("Claude 3 Haiku", "claude-3-haiku-20240307"),
            ],
            "OPENAI": [
                ("GPT-4 Turbo", "gpt-4-0125-preview"),
                ("GPT-3.5", "gpt-3.5-turbo-0125"),
            ],
            "GOOGLE": [
                ("Gemini 1.0 Pro", "gemini-pro"),
            ],
            "MISTRAL": [
                ("Mistral 7b", "open-mistral-7b"),
                ("Mistral 8x7b", "open-mixtral-8x7b"),
                ("Mistral Medium", "mistral-medium-latest"),
                ("Mistral Small", "mistral-small-latest"),
                ("Mistral Large", "mistral-large-latest"),
            ],
            "OLLAMA_MODELS": []
        }
        if ollama:
            self.models["OLLAMA_MODELS"] = [(model["name"].split(":")[0], model["name"]) for model in
                                            ollama.list_models()]
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d

    def list_models(self) -> dict:
        return self.models

<<<<<<< HEAD
    def update_global_token_usage(self, string: str, project_name: str):
        token_usage = len(TIKTOKEN_ENC.encode(string))
        AgentState().update_token_usage(project_name, token_usage)

    def inference(
        self, prompt: str, project_name: str
    ) -> str:
        self.update_global_token_usage(prompt, project_name)
        
        model = self.model_id_to_enum_mapping()[self.model_id]

        if self.log_prompts:
            logger.debug(f"Prompt ({model}): --> {prompt}")

        if model == "OLLAMA_MODELS":
            response = Ollama().inference(self.model_id, prompt).strip()
        elif "CLAUDE" in str(model):
            response = Claude().inference(self.model_id, prompt).strip()
        elif "GPT" in str(model):
            response = OpenAI().inference(self.model_id, prompt).strip()
        elif "GROQ" in str(model):
            response = Groq().inference(self.model_id, prompt).strip()
        else:
            raise ValueError(f"Model {model} not supported")

        if self.log_prompts:
            logger.debug(f"Response ({model}): --> {response}")

        self.update_global_token_usage(response, project_name)
        
=======
    def model_id_to_enum_mapping(self) -> dict:
        mapping = {}
        for enum_name, models in self.models.items():
            for model_name, model_id in models:
                mapping[model_id] = enum_name
        return mapping

    @staticmethod
    def update_global_token_usage(string: str):
        global TOKEN_USAGE
        TOKEN_USAGE += len(TIKTOKEN_ENC.encode(string))
        emit_agent("tokens", {"token_usage": TOKEN_USAGE})
        print(f"Token usage: {TOKEN_USAGE}")

    def inference(self, prompt: str) -> str:
        self.update_global_token_usage(prompt)

        model_enum = self.model_id_to_enum_mapping().get(self.model_id)
        if model_enum is None:
            raise ValueError(f"Model {self.model_id} not supported")

        model_mapping = {
            "OLLAMA_MODELS": ollama,
            "CLAUDE": Claude(),
            "OPENAI": OpenAi(),
            "GOOGLE": Gemini(),
            "MISTRAL": MistralAi()
        }

        try:
            model = model_mapping[model_enum]
            response = model.inference(self.model_id, prompt).strip()
        except KeyError:
            raise ValueError(f"Model {model_enum} not supported")

        self.update_global_token_usage(response)

>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
        return response
