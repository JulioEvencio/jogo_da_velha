_ERRO = -1
_SUCESSO = 0
_VAZIO = ' '
_TABULEIRO_LINHA = 3
_TABULEIRO_COLUNA = 3
_PLAYER_1_GANHOU = 1
_PLAYER_2_GANHOU = 2
_EMPATE = 3

class Tabuleiro:
    def __init__(self):
        self.__tabuleiro = [
            [_VAZIO, _VAZIO, _VAZIO],
            [_VAZIO, _VAZIO, _VAZIO],
            [_VAZIO, _VAZIO, _VAZIO]
        ]

    def printarTabuleiro(self):
        print('-|1|2|3')
        print('A|{}|{}|{}'.format(self.__tabuleiro[0][0], self.__tabuleiro[0][1], self.__tabuleiro[0][2]))
        print('B|{}|{}|{}'.format(self.__tabuleiro[1][0], self.__tabuleiro[1][1], self.__tabuleiro[1][2]))
        print('C|{}|{}|{}'.format(self.__tabuleiro[2][0], self.__tabuleiro[2][1], self.__tabuleiro[2][2]))

    def fazerJogada(self, linha, coluna, simbolo):
        if(linha == _ERRO or coluna == _ERRO):
            return _ERRO
        if(self.__tabuleiro[linha][coluna] != _VAZIO):
            return _ERRO
        self.__tabuleiro[linha][coluna] = simbolo
        return _SUCESSO

    def __verificarPosicaoVazia(self):
        for linha in range(_TABULEIRO_LINHA):
            for coluna in range(_TABULEIRO_COLUNA):
                if(self.__tabuleiro[linha][coluna] == _VAZIO):
                    return True
        return False

    def verificarGanhador(self, p1, p2):
        #   Jogador 1
        #   Linha
        for i in range(_TABULEIRO_LINHA):
            if(self.__tabuleiro[i][0] == p1 and self.__tabuleiro[i][1] == p1 and self.__tabuleiro[i][2] == p1): return _PLAYER_1_GANHOU
        #   Coluna
        for i in range(_TABULEIRO_COLUNA):
            if(self.__tabuleiro[0][i] == p1 and self.__tabuleiro[1][i] == p1 and self.__tabuleiro[2][i] == p1): return _PLAYER_1_GANHOU
        #   Diagonal
        if(self.__tabuleiro[0][0] == p1 and self.__tabuleiro[1][1] == p1 and self.__tabuleiro[2][2] == p1): return _PLAYER_1_GANHOU
        if(self.__tabuleiro[2][0] == p1 and self.__tabuleiro[1][1] == p1 and self.__tabuleiro[0][2] == p1): return _PLAYER_1_GANHOU

        #   Jogador 2
        #   Linha
        for i in range(_TABULEIRO_LINHA):
            if(self.__tabuleiro[i][0] == p2 and self.__tabuleiro[i][1] == p2 and self.__tabuleiro[i][2] == p2): return _PLAYER_2_GANHOU
        #   Coluna
        for i in range(_TABULEIRO_COLUNA):
            if(self.__tabuleiro[0][i] == p2 and self.__tabuleiro[1][i] == p2 and self.__tabuleiro[2][i] == p2): return _PLAYER_2_GANHOU
        #   Diagonal
        if(self.__tabuleiro[0][0] == p2 and self.__tabuleiro[1][1] == p2 and self.__tabuleiro[2][2] == p2): return _PLAYER_2_GANHOU
        if(self.__tabuleiro[2][0] == p2 and self.__tabuleiro[1][1] == p2 and self.__tabuleiro[0][2] == p2): return _PLAYER_2_GANHOU

        if(self.__verificarPosicaoVazia()):
            return False
        
        return _EMPATE
