import pygame as pg
from lista_simples import ListaSimples
from lista_simples_ordenada import ListaSimplesOrdenada

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class App:

    def __init__(self):
        pg.init()
        window = pg.display.set_mode((800, 600))
        pg.display.set_caption("Data Structures Visualizer")
        self.text_addr_font = pg.font.SysFont("Arial", 14)
        self.text_chave_font = pg.font.SysFont("Arial", 64)
        self.main_loop(window)

    def main_loop(self, window):
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.quit:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                       running = False 

            window.fill(BLACK)
            no_exemplo = pg.Rect(100, 100, 100, 120)
            pg.draw.rect(window, WHITE, no_exemplo, width = 2)
            pg.draw.line(window, WHITE, (100, 120), (197, 120), 3)
            pg.draw.line(window, WHITE, (100, 200), (197, 200), 3)
            self.draw_text(window, "0x7FFE4", self.text_addr_font, RED, 98, 78) # own memory addr
            self.draw_text(window, "0x7FFE4", self.text_addr_font, WHITE, 122, 102) # prox memory addr
            self.draw_text(window, "1", self.text_chave_font, WHITE, 132, 125) # chave
            self.draw_text(window, "0x7FFE4", self.text_addr_font, WHITE, 122, 202) # ant memory addr
            pg.display.flip()

        pg.quit()

    def draw_text(self, window, text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        window.blit(img, (x, y))

    def draw_no(self, window, ch, x, y):
        rectangle = pg.Rect(50, 50, x, y) 
        pg.draw.rect(window, WHITE, rectangle, width = 2)

    def draw_pointer_arrow(self, window, n1, n2):
        pass

if __name__ == "__main__":
    app = App()
