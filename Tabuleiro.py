_VAZIO = ' '

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
