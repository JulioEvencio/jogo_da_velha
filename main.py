from Tabuleiro import Tabuleiro, _PLAYER_1_GANHOU, _PLAYER_2_GANHOU, _EMPATE
from Player import Player
from funcoes import jogar

tabuleiro = Tabuleiro()
j1 = Player('Fulano', 'O')
j2 = Player('Ciclano', 'X')
jogar(tabuleiro, j1, j2)
