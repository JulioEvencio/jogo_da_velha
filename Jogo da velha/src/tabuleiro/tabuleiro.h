#ifndef TABULEIRO_H_INCLUDED
#define TABULEIRO_H_INCLUDED

#define TABULEIRO_GAME_OVER 1
#define TABULERIO_EMPATE '\0'

typedef struct Tabuleiro Tabuleiro;

int tabuleiro_criar(Tabuleiro **tabuleiro);
void tabuleiro_liberar(Tabuleiro **tabuleiro);

int tabulerio_fazer_jogada(Tabuleiro **tabuleiro, int linha, int coluna, char simbolo);
char tabuleiro_verificar_game_over(Tabuleiro **tabuleiro, char *simbolo);
char tabulerio_obter(Tabuleiro **tabuleiro, int linha, int coluna);

#endif