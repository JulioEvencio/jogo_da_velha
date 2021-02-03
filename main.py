from Tabuleiro import Tabuleiro, _PLAYER_1_GANHOU, _PLAYER_2_GANHOU, _EMPATE
from Player import Player

tabuleiro = Tabuleiro()
j1 = Player('Fulano', 'O')
j2 = Player('Ciclano', 'X')
vez = 1
vitoria = 0
while(True):
    tabuleiro.printarTabuleiro()
    if(vez % 2 != 0):
        print('Jogador 1')
        j1.fazerJogada()
        if(not tabuleiro.fazerJogada(j1.linha, j1.coluna, j1.simbolo)):
            vez += 1
    else:
        print('Jogador 2')
        j2.fazerJogada()
        if(not tabuleiro.fazerJogada(j2.linha, j2.coluna, j2.simbolo)):
            vez += 1
    vitoria = tabuleiro.verificarGanhador(j1.simbolo, j2.simbolo)
    if(vitoria):
        if(vitoria == _PLAYER_1_GANHOU):
            print('Jogador 1 ganhou!')
            break
        elif(vitoria == _PLAYER_2_GANHOU):
            print('jogador 2 ganhou!')
            break
        else:
            print('Empate!')
            break
    print('---------------------------')
    print('---------------------------')
    print('---------------------------')
