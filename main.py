import os
from Tabuleiro import Tabuleiro
from Player import Player
from funcoes import jogar, menu, rank, _OPCAO_SAIR, _OPCAO_JOGAR, _OPCAO_RANK

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
    os.system('cls' if os.name == 'nt' else 'clear')
    opcao = menu()
    
    if(opcao == _OPCAO_JOGAR):
        jogar(tabuleiro, j1, j2)
    elif(opcao == _OPCAO_RANK):
        rank(j1, j2)
    elif(opcao == _OPCAO_SAIR):
        print('Obrigado por jogar!')
        loop = False
    else:
        print('Opção inválida!')
        input('Pressione enter para continuar...')
