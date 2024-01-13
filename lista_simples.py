from no import No

class ListaSimples():
    def __init__(self):
        self.inicio = None

    def insere(self, ch):
        if self.inicio == None:
            self.inicio = No(ch) 
            return True

        novo = No(ch)
        novo.prox = self.inicio
        self.inicio = novo
        return True

    def __busca_aux(self, ch, ant):
        atual = self.inicio

        while atual:
            if atual.ch == ch:
                return atual

            ant = atual
            atual = atual.prox

        return None

    def exclui(self, ch):
        ant = self.inicio 
        atual = self.__busca_aux(ch, ant)

        if not atual:
            print("O item a ser deletado nao existe na lista")
            return False

        ant.prox = atual.prox

        return True


    def exibe(self):
        if self.inicio == None:
            print("Vazia")
            return
        atual = self.inicio
        while atual:
            print(str(atual.ch), end="")
            atual = atual.prox
        print("\n")
