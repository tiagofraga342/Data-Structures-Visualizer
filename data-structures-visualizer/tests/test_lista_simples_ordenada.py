import unittest
from ..listas.lista_simples_ordenada import ListaSimplesOrdenada

class TestListaSimplesOrdenada(unittest.TestCase):

    def test_inicializacao(self):
        lista = ListaSimplesOrdenada()
        self.assertIsNone(lista.inicio)

    def test_insercao(self):
        lista = ListaSimplesOrdenada()
        lista.insere(3)
        lista.insere(4)
        lista.insere(2)
        lista.insere(1) # [1, 2, 3, 4]

        self.assertEqual(lista.inicio.ch, 1)

    def test_exclusao_inicio(self):
        lista = ListaSimplesOrdenada()
        lista.insere(1)
        lista.insere(2)
        lista.insere(3) # [1, 2, 3]
        lista.exclui(1) # [2, 3]

        self.assertEqual(lista.inicio.ch, 2)
        self.assertEqual(lista.inicio.prox.ch, 3)

    def test_exclusao_meio(self):
        lista = ListaSimplesOrdenada()
        lista.insere(1)
        lista.insere(2)
        lista.insere(3) # [1, 2, 3]
        lista.exclui(2) # [1, 3]

        self.assertEqual(lista.inicio.ch, 1)
        self.assertEqual(lista.inicio.prox.ch, 3)

    def test_exclusao_fim(self):
        lista = ListaSimplesOrdenada()
        lista.insere(1)
        lista.insere(2)
        lista.insere(3) # [1, 2, 3]
        lista.exclui(3) # [1, 2]

        self.assertEqual(lista.inicio.ch, 1)
        self.assertEqual(lista.inicio.prox.ch, 2)

    def test_exclusao_item_inexistente(self):
        lista = ListaSimplesOrdenada()
        lista.insere(1)

        self.assertFalse(lista.exclui(0))

    def test_exclusao_lista_vazia(self):
        lista = ListaSimplesOrdenada()
        
        self.assertFalse(lista.exclui(1))

if __name__ == "__main__":
    unittest.main()
