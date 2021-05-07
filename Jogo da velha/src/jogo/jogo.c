#include <stdlib.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include "../jogo_da_velha.h"
#include "../tabuleiro/tabuleiro.h"
#include "jogo.h"

#define JOGO_COR_PRETA 0, 0, 0, 255
#define JOGO_VEZ_X 0
#define JOGO_VEZ_O 1

struct Jogo
{
    int vez;
    Tabuleiro *tabuleiro;
    SDL_Texture *jogador;
    SDL_Texture *adversario;
};

int jogo_criar(Jogo **jogo, SDL_Texture **textura)
{
    *jogo = malloc(sizeof **jogo);

    if (*jogo == NULL) return -1;

    if (tabuleiro_criar(&(*jogo)->tabuleiro)) return -1;

    (*jogo)->vez = JOGO_VEZ_X;
    (*jogo)->jogador = textura[TEXTURA_X];
    (*jogo)->adversario = textura[TEXTURA_O];

    return 0;
}

void jogo_liberar(Jogo **jogo)
{
    tabuleiro_liberar(&(*jogo)->tabuleiro);
    free(*jogo);
}

void jogo_tela(Jogo **jogo, SDL_Renderer *tela)
{
    int quadrado_x, quadrado_y;
    int quadrado_largura = JANELA_LARGURA / TABULEIRO_COLUNA;
    int quadrado_altura = JANELA_ALTURA / TABULEIRO_LINHA;

    for (int linha = 0; linha < TABULEIRO_LINHA; linha++)
    {
        for (int coluna = 0; coluna < TABULEIRO_COLUNA; coluna++)
        {
            quadrado_x = coluna * quadrado_largura;
            quadrado_y = linha * quadrado_altura;

            SDL_Rect quadrado = {quadrado_x, quadrado_y, quadrado_largura, quadrado_altura};

            if (tabulerio_obter_simbolo(&(*jogo)->tabuleiro, linha, coluna) == 'x')
            {
                SDL_RenderCopy(tela, (*jogo)->jogador, NULL, &quadrado);
            }

            if (tabulerio_obter_simbolo(&(*jogo)->tabuleiro, linha, coluna) == 'o')
            {
                SDL_RenderCopy(tela, (*jogo)->adversario, NULL, &quadrado);
            }

            SDL_SetRenderDrawColor(tela, JOGO_COR_PRETA);
            SDL_RenderDrawRect(tela, &quadrado);
        }
    }
}

void jogo_evento(Jogo **jogo, SDL_Event *evento)
{
    if (evento->type == SDL_MOUSEBUTTONDOWN)
    {
        int mouse_coluna = evento->motion.x / (JANELA_LARGURA / TABULEIRO_COLUNA);
        int mouse_linha = evento->motion.y / (JANELA_ALTURA / TABULEIRO_LINHA);

        if ((*jogo)->vez == JOGO_VEZ_X)
        {
            tabulerio_fazer_jogada(&(*jogo)->tabuleiro, mouse_linha, mouse_coluna, 'x');
            (*jogo)->vez = JOGO_VEZ_O;
        }
        else
        {
            tabulerio_fazer_jogada(&(*jogo)->tabuleiro, mouse_linha, mouse_coluna, 'o');
            (*jogo)->vez = JOGO_VEZ_X;
        }
    }
}