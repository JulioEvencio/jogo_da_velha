import os
from Tabuleiro import _PLAYER_1_GANHOU, _PLAYER_2_GANHOU

_OPCAO_SAIR = 0
_OPCAO_JOGAR = 1
_OPCAO_RANK = 2

def menu():
    print('--------MENU----------')
    print('1. Jogar')
    print('2. Rank')
    print('0. Sair')
    opcao = int(input('Opção: '))
    return opcao

def rank(j1, j2):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--------RANK----------')
    j1.getPlayer()
    print('---------------------------')
    j2.getPlayer()
    print('---------------------------')
    input('Pressione enter para continuar...')

def jogar(tabuleiro, j1, j2):
    vez = 1
    vitoria = 0
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro.printarTabuleiro()
        if(vez % 2 != 0):
            print('Vez de {}'.format(j1.nome))
            j1.fazerJogada()
            if(tabuleiro.fazerJogada(j1.linha, j1.coluna, j1.simbolo)):
                print('Posição inválida!')
                print('---------------------------')
                input('Pressione enter para continuar...')
            else:
                vez += 1
        else:
            print('Vez de {}'.format(j2.nome))
            j2.fazerJogada()
            if(tabuleiro.fazerJogada(j2.linha, j2.coluna, j2.simbolo)):
                print('Posição inválida!')
                print('---------------------------')
                input('Pressione enter para continuar...')
            else:
                vez += 1
        vitoria = tabuleiro.verificarGanhador(j1.simbolo, j2.simbolo)
        if(vitoria):
            if(vitoria == _PLAYER_1_GANHOU):
                os.system('cls' if os.name == 'nt' else 'clear')
                tabuleiro.printarTabuleiro()
                print('Jogador 1 ganhou!')
                j1.vitoria += 1
                j2.derrota += 1
                print('---------------------------')
                input('Pressione enter para continuar...')
                break
            elif(vitoria == _PLAYER_2_GANHOU):
                os.system('cls' if os.name == 'nt' else 'clear')
                tabuleiro.printarTabuleiro()
                print('jogador 2 ganhou!')
                j2.vitoria += 1
                j1.derrota += 1
                print('---------------------------')
                input('Pressione enter para continuar...')
                break
            else:
                print('Empate!')
                j1.empate += 1
                j2.empate += 1
                print('---------------------------')
                input('Pressione enter para continuar...')
                break
