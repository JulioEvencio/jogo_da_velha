from Tabuleiro import Tabuleiro
from Player import Player
from funcoes import jogar

nome = input('Digite seu nome: ')
simbolo = input('Digite seu símbolo no jogo')

tabuleiro = Tabuleiro()
j1 = Player(nome, simbolo)
j2 = Player('Ciclano', 'X')
jogar(tabuleiro, j1, j2)
