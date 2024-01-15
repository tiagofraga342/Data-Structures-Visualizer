import unittest
from ..listas.lista_simples import ListaSimples 

class TestListaSimples(unittest.TestCase):
    
    def test_inicializacao(self):
        lista = ListaSimples() 

        self.assertIsNone(lista.inicio)

    def test_insercao(self):
        lista = ListaSimples()
        lista.insere(1)
        lista.insere(2)

        self.assertEqual(lista.inicio.ch, 2)
        self.assertEqual(lista.inicio.prox.ch, 1)

    def test_exclusao_inicio(self):
        lista = ListaSimples()
        lista.insere(3)
        lista.insere(1) # [1, 3]
        lista.exclui(3) # [1]

        self.assertEqual(lista.inicio.ch, 1)

    def test_exclusao_meio(self):
        lista = ListaSimples()
        lista.insere(1)
        lista.insere(2)
        lista.insere(3) # [3, 2, 1]
        lista.exclui(2) # [3, 1]

        self.assertEqual(lista.inicio.ch, 3)
        self.assertEqual(lista.inicio.prox.ch, 1)

    def test_exclusao_fim(self):
        lista = ListaSimples()
        lista.insere(1)
        lista.insere(2)
        lista.exclui(2)

        self.assertIsNone(lista.inicio.prox)

    def test_exclusao_item_inexistente(self):
        lista = ListaSimples()
        lista.insere(1)

        self.assertFalse(lista.exclui(0))

    def test_exclusao_lista_vazia(self):
        lista = ListaSimples()

        self.assertFalse(lista.exclui(1))        

if __name__ == "__main__":
    unittest.main()
