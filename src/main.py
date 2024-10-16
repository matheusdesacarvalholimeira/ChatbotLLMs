import os
from src.chatbot import criar_chatbot, interagir
from src.document_loader import carregar_documento_e_criar_indice
from src.config import Config

Config.validate()

def main():
    chatbot = criar_chatbot()
    caminho_documento = os.path.join("data", "knowledge_base.txt")
    indice = carregar_documento_e_criar_indice(caminho_documento)

    print("Digite 'sair' para encerrar.")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == 'sair':
            print("Encerrando o chatbot. Até logo!")
            break

        resposta_documento = consultar_indice(pergunta, indice)
        resposta_chatbot = interagir(pergunta, chatbot)

        print(f"Resposta do documento: {resposta_documento}")
        print(f"Resposta do Chatbot: {resposta_chatbot}")

if __name__ == "__main__":
    main()