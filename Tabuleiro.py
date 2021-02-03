_ERRO = -1
_SUCESSO = 0
_VAZIO = ' '
_TABULEIRO_LINHA = 3
_TABULEIRO_COLUNA = 3

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
            print('Posição inválida!')
            return _ERRO
        if(self.__tabuleiro[linha][coluna] != _VAZIO):
            print('Posição inválida!')
            return _ERRO
        self.__tabuleiro[linha][coluna] = simbolo
        return _SUCESSO

    def __verificarPosicaoVazia(self):
        for linha in range(_TABULEIRO_LINHA):
            for coluna in range(_TABULEIRO_COLUNA):
                if(self.__tabuleiro[linha][coluna] == _VAZIO):
                    return 1
        return 0

    def verificarGanhador(self, p1, p2):
        #   Jogador 1
        #   Linha
        for i in range(_TABULEIRO_LINHA):
            if(self.__tabuleiro[i][0] == p1 and self.__tabuleiro[i][1] == p1 and self.__tabuleiro[i][2] == p1): return 1
        #   Coluna
        for i in range(_TABULEIRO_COLUNA):
            if(self.__tabuleiro[0][i] == p1 and self.__tabuleiro[1][i] == p1 and self.__tabuleiro[2][i] == p1): return 1
        #   Diagonal
        if(self.__tabuleiro[0][0] == p1 and self.__tabuleiro[1][1] == p1 and self.__tabuleiro[2][2] == p1): return 1
        if(self.__tabuleiro[2][0] == p1 and self.__tabuleiro[1][1] == p1 and self.__tabuleiro[0][2] == p1): return 1

        #   Jogador 2
        #   Linha
        for i in range(_TABULEIRO_LINHA):
            if(self.__tabuleiro[i][0] == p2 and self.__tabuleiro[i][1] == p2 and self.__tabuleiro[i][2] == p2): return 2
        #   Coluna
        for i in range(_TABULEIRO_COLUNA):
            if(self.__tabuleiro[0][i] == p2 and self.__tabuleiro[1][i] == p2 and self.__tabuleiro[2][i] == p2): return 2
        #   Diagonal
        if(self.__tabuleiro[0][0] == p2 and self.__tabuleiro[1][1] == p2 and self.__tabuleiro[2][2] == p2): return 2
        if(self.__tabuleiro[2][0] == p2 and self.__tabuleiro[1][1] == p2 and self.__tabuleiro[0][2] == p2): return 2
