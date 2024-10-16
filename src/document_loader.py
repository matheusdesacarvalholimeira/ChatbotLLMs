from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def carregar_documento_e_criar_indice(caminho_arquivo):
    loader = TextLoader(caminho_arquivo)
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index

def consultar_indice(pergunta, index):
    return index.query(pergunta)