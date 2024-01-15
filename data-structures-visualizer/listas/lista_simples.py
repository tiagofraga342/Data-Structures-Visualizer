from .no_lista import NoSimples

class ListaSimples():
    def __init__(self):
        self.inicio = None

    def insere(self, ch):
        if self.inicio == None:
            self.inicio = NoSimples(ch) 
            return True

        novo = NoSimples(ch)
        novo.prox = self.inicio
        self.inicio = novo

        return True

    def __busca_aux(self, ch):
        ant = None
        atual = self.inicio

        while atual:
            if atual.ch == ch:
                return ant, atual

            ant = atual
            atual = atual.prox

        return None, None

    def exclui(self, ch):
        ant, atual = self.__busca_aux(ch)

        if not atual:
            print("ERRO: o item a ser deletado nao existe na lista")
            return False

        if ant:
            ant.prox = atual.prox
        else:
            self.inicio = atual.prox

        return True


    def exibe(self):
        if self.inicio == None:
            print("Vazia")
            return
        atual = self.inicio
        while atual:
            print(str(atual.ch), end=", ")
            atual = atual.prox
        print("\n")
