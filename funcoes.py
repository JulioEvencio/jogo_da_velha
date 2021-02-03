_VAZIO = ' '
_TABULEIRO_LINHA = 3
_TABULEIRO_COLUNA = 3

def criar_tabuleiro():
    tabuleiro = [
        [_VAZIO, _VAZIO, _VAZIO],
        [_VAZIO, _VAZIO, _VAZIO],
        [_VAZIO, _VAZIO, _VAZIO]
    ]
    return tabuleiro

def printar_tabuleiro(tabuleiro):
    print('-|1|2|3')
    print('A|{}|{}|{}'.format(tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print('B|{}|{}|{}'.format(tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print('C|{}|{}|{}'.format(tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))
