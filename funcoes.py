import os
from Tabuleiro import Tabuleiro
from Tabuleiro import _PLAYER_1_GANHOU, _PLAYER_2_GANHOU

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
                break
            elif(vitoria == _PLAYER_2_GANHOU):
                os.system('cls' if os.name == 'nt' else 'clear')
                tabuleiro.printarTabuleiro()
                print('jogador 2 ganhou!')
                j2.vitoria += 1
                j1.derrota += 1
                break
            else:
                print('Empate!')
                j1.empate += 1
                j2.empate += 1
                break
