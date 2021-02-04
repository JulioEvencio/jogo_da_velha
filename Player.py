_ERRO = -1

class Player:
    def __init__(self, nome, simbolo):
        self.__nome = nome
        self.simbolo = simbolo
        self.vitoria = 0
        self.derrota = 0
        self.empate = 0
        self.linha = _ERRO
        self.coluna = _ERRO

    def getPlayer(self):
        print('Nome: {}'.format(self.__nome))
        print('Símbolo: {}'.format(self.simbolo))
        print('Vitórias: {}'.format(self.vitoria))
        print('Derrotas: {}'.format(self.derrota))
        print('Empates: {}'.format(self.empate))

    def __lerLinha(self):
        linha = input('Letra: ')
        if(linha == 'a' or linha == 'A'): return 0
        if(linha == 'b' or linha == 'B'): return 1
        if(linha == 'c' or linha == 'C'): return 2
        return _ERRO

    def __lerColuna(self):
        coluna = int(input('Número: '))
        if(coluna >= 1 and coluna <= 3): return (coluna - 1)
        else: return _ERRO

    def fazerJogada(self):
        self.linha = self.__lerLinha()
        self.coluna = self.__lerColuna()
