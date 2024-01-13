import pygame
from lista_simples import ListaSimples
from lista_simples_ordenada import ListaSimplesOrdenada

lista = ListaSimplesOrdenada()
lista.insere(1)
lista.insere(5)
lista.insere(2)
lista.exibe()

lista.exclui(5)
lista.exibe()
