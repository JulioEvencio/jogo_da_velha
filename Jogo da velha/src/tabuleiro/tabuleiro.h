#ifndef TABULEIRO_H_INCLUDED
#define TABULEIRO_H_INCLUDED

#define TABULEIRO_LINHA 3
#define TABULEIRO_COLUNA 3
#define TABULEIRO_GAME_OVER 1
#define TABULERIO_POSICAO_VAZIA '\0'

typedef struct Tabuleiro Tabuleiro;

int tabuleiro_criar(Tabuleiro **tabuleiro);
void tabuleiro_liberar(Tabuleiro **tabuleiro);
void tabuleiro_resetar(Tabuleiro **tabuleiro);

int tabulerio_fazer_jogada(Tabuleiro **tabuleiro, int linha, int coluna, char simbolo);
int tabuleiro_verificar_game_over(Tabuleiro **tabuleiro, char *simbolo);
char tabulerio_obter_simbolo(Tabuleiro **tabuleiro, int linha, int coluna);

#endif