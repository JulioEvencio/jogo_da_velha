from Tabuleiro import Tabuleiro
from Player import Player

tabuleiro = Tabuleiro()
tabuleiro.printarTabuleiro()

j1 = Player("Fulano", 'O')
j1.fazerJogada()

tabuleiro.fazerJogada(j1.linha, j1.coluna, j1.simbolo)
tabuleiro.printarTabuleiro()
