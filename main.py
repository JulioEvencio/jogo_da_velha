from Tabuleiro import Tabuleiro
from Player import Player

tabuleiro = Tabuleiro()
j1 = Player('Fulano', 'O')
j2 = Player('Ciclano', 'X')
vez = 1
while(vez < 10):
    tabuleiro.printarTabuleiro()
    if(vez % 2 != 0):
        print('Jogador 1')
        j1.fazerJogada()
        if(tabuleiro.fazerJogada(j1.linha, j1.coluna, j1.simbolo)):
            vez += 1
    else:
        print('Jogador 2')
        j2.fazerJogada()
        if(tabuleiro.fazerJogada(j2.linha, j2.coluna, j2.simbolo)):
            vez += 1
    print('---------------------------')
    print('---------------------------')
    print('---------------------------')
