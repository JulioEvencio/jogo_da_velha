import os
from Tabuleiro import Tabuleiro
from Player import Player
from funcoes import jogar

os.system('cls' if os.name == 'nt' else 'clear')
tabuleiro = Tabuleiro()

nome = input('Nome do jogador 1: ')
simbolo = input('Símbolo do joador 1: ')
j1 = Player(nome, simbolo)

nome = input('Nome do jogador 2: ')
simbolo = input('Símbolo do joador 2: ')
j2 = Player(nome, simbolo)

loop = True

while(loop):
    jogar(tabuleiro, j1, j2)
    j1.getPlayer()
    j2.getPlayer()
