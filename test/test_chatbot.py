import unittest
from src.chatbot import criar_chatbot, interagir

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = criar_chatbot()

    def test_interacao_simples(self):
        resposta = interagir("Qual é a capital da França?", self.chatbot)
        self.assertIsInstance(resposta, str)
        self.assertGreater(len(resposta), 0)

if __name__ == '__main__':
    unittest.main()