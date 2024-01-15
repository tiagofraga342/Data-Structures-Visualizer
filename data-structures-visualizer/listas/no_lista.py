class NoSimples:

    def __init__(self, ch):
        self.ch = ch
        self.prox = None

    def draw_no(self, window):
        pass

class NoDuplamenteLigado(NoSimples):

    def __init__(self):
        self.ant = None
