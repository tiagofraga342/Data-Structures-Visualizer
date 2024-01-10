import pygame
from lista_simples import ListaSimples

lista = ListaSimples()
lista.insere(1)
lista.insere(5)
lista.insere(2)
lista.exibe()

lista.exclui(5)
lista.exibe()
