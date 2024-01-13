from no import No
from lista_simples import ListaSimples

class ListaSimplesOrdenada(ListaSimples):
    def __init__(self):
        self.inicio = None

    def insere(self, ch):
        ant = self.inicio
        atual = self.__busca_aux_insere(ant, ch)

        if atual:
            print("O item a ser inserido ja esta presente na lista")
            return False
        
        atual = No(ch)

        if ant:
            atual.prox = ant.prox
            ant.prox = atual
        else:
            atual.prox = self.inicio
            self.inicio = atual

        return True

    def exclui(self, ch):
        ant, atual = self.__busca_aux_exclui(ch)

        if not atual:
            print("O item a ser excluido nao existe na lista")
            return False

        if ant:
            ant.prox = atual.prox
        else:
            self.inicio = atual.prox
        
        return True

    def __busca_aux_exclui(self, ch):
        ant = None 
        atual = self.inicio

        while atual and atual.ch < ch:
            ant = atual
            atual = atual.prox

        if atual and atual.ch == ch:
            return ant, atual

        return None, None

    def __busca_aux_insere(self, ant, ch):
        atual = self.inicio

        while atual and atual.ch < ch:
            ant = atual
            atual = atual.prox

        if atual and atual.ch == ch:
            return atual

        return None
