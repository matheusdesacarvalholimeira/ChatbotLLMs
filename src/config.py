import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ValueError("A chave de API da OpenAI não está configurada.")