from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from src.config import Config


def criar_llm():
    return OpenAI(api_key=Config.OPENAI_API_KEY)

def criar_chatbot():
    llm = criar_llm()
    memory = ConversationBufferMemory()
    return ConversationChain(llm=llm, memory=memory)

def interagir(pergunta, chatbot):
    return chatbot.run(input=pergunta)