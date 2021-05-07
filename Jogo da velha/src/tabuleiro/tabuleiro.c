#include <stdlib.h>
#include "tabuleiro.h"

int tabulerio_verificar_posicao_vazia(Tabuleiro **tabuleiro);

struct Tabuleiro
{
    char tabuleiro[TABULEIRO_LINHA][TABULEIRO_COLUNA];
};

int tabuleiro_criar(Tabuleiro **tabuleiro)
{
    *tabuleiro = malloc(sizeof **tabuleiro);

    if (*tabuleiro == NULL) return -1;

    tabuleiro_resetar(tabuleiro);

    return 0;
}

void tabuleiro_liberar(Tabuleiro **tabuleiro)
{
    free(*tabuleiro);
}

void tabuleiro_resetar(Tabuleiro **tabuleiro)
{
    for (int linha = 0; linha < TABULEIRO_LINHA; linha++)
    {
        for (int coluna = 0; coluna < TABULEIRO_COLUNA; coluna++)
        {
            (*tabuleiro)->tabuleiro[linha][coluna] = TABULERIO_EMPATE;
        }
    }
}

int tabulerio_fazer_jogada(Tabuleiro **tabuleiro, int linha, int coluna, char simbolo)
{
    if (linha < 0 || linha >= TABULEIRO_LINHA) return -1;
    if (coluna < 0 || linha >= TABULEIRO_COLUNA) return -1;
    if (simbolo == TABULERIO_EMPATE) return -1;

    (*tabuleiro)->tabuleiro[linha][coluna] = simbolo;

    return 0;
}

int tabulerio_verificar_posicao_vazia(Tabuleiro **tabuleiro)
{
    for (int linha = 0; linha < TABULEIRO_LINHA; linha++)
    {
        for (int coluna = 0; coluna < TABULEIRO_COLUNA; coluna++)
        {
            if ((*tabuleiro)->tabuleiro[linha][coluna] == TABULERIO_EMPATE)
            {
                return 1;
            }
        }
    }

    return 0;
}

int tabuleiro_verificar_game_over(Tabuleiro **tabuleiro, char *simbolo)
{
    /* Linha */
    for (int i = 0; i < TABULEIRO_LINHA; i++)
    {
        if ((*tabuleiro)->tabuleiro[i][0] == (*tabuleiro)->tabuleiro[i][1] && (*tabuleiro)->tabuleiro[i][1] == (*tabuleiro)->tabuleiro[i][2])
        {
            *simbolo = (*tabuleiro)->tabuleiro[i][0];
            return TABULEIRO_GAME_OVER;
        }
    }

    /* Coluna */
    for (int i = 0; i < TABULEIRO_COLUNA; i++)
    {
        if ((*tabuleiro)->tabuleiro[0][i] == (*tabuleiro)->tabuleiro[1][i] && (*tabuleiro)->tabuleiro[1][i] == (*tabuleiro)->tabuleiro[2][i])
        {
            *simbolo = (*tabuleiro)->tabuleiro[0][i];
            return TABULEIRO_GAME_OVER;
        }
    }

    /* Diagonal Principal */
    if ((*tabuleiro)->tabuleiro[0][0] == (*tabuleiro)->tabuleiro[1][1] && (*tabuleiro)->tabuleiro[1][1] == (*tabuleiro)->tabuleiro[2][2])
    {
        *simbolo = (*tabuleiro)->tabuleiro[1][1];
        return TABULEIRO_GAME_OVER;
    }

    /* Diagonal Segundaria */
    if ((*tabuleiro)->tabuleiro[2][0] == (*tabuleiro)->tabuleiro[1][1] && (*tabuleiro)->tabuleiro[1][1] == (*tabuleiro)->tabuleiro[0][2])
    {
        *simbolo = (*tabuleiro)->tabuleiro[1][1];
        return TABULEIRO_GAME_OVER;
    }

    if (tabulerio_verificar_posicao_vazia(tabuleiro))
    {
        return 0;
    }

    *simbolo = TABULERIO_EMPATE;
    return TABULEIRO_GAME_OVER;
}

char tabulerio_obter_simbolo(Tabuleiro **tabuleiro, int linha, int coluna)
{
    return (*tabuleiro)->tabuleiro[linha][coluna];
}