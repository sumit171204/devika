<<<<<<< HEAD
import httpx
from ollama import Client
from src.config import Config

from src.logger import Logger

logger = Logger()

client = Client(host=Config().get_ollama_api_endpoint())
=======
import ollama
from src.logger import Logger

log = Logger()
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d


class Ollama:
    def __init__(self):
        try:
<<<<<<< HEAD
            return client.list()["models"]
        except httpx.ConnectError:
            logger.warning("Ollama server not running, please start the server to use models from Ollama.")
        except Exception as e:
            logger.error(f"Failed to list Ollama models: {e}")
        return []

    def inference(self, model_id: str, prompt: str) -> str:
        try:
            response = ollama.generate(model=model_id, prompt=prompt.strip())
            return response['response']
        except Exception as e:
            logger.error(f"Error during model inference: {e}")
        return ""
=======
            self.client = ollama.Client()
            log.info("Ollama available")
        except:
            self.client = None
            log.warning("Ollama not available")
            log.warning("run ollama server to use ollama models otherwise use other models")

    def list_models(self) -> list[dict]:
        models = self.client.list()["models"]
        return models

    def inference(self, model_id: str, prompt: str) -> str:
        response = self.client.generate(
            model=model_id,
            prompt=prompt.strip()
        )
        return response['response']
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
