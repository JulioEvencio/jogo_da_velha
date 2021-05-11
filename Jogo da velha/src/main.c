#include <stdio.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include "jogo_da_velha.h"
#include "jogo/jogo.h"

int main(int argc, char *argv[])
{
    int loop = 1;

    Jogo *jogo = NULL;

    SDL_Window *janela = NULL;
    SDL_Renderer *tela = NULL;
    SDL_Texture *textura[TEXTURA_QUANTIDADE];
    SDL_Event evento;

    if (SDL_Init(SDL_INIT_VIDEO) < 0)
    {
        puts("Erro ao inicializar SDL 2!");
        return 1;
    }

    if (IMG_Init(IMG_INIT_PNG) < 0)
    {
        puts("Erro ao inicializar SDL Image!");
        SDL_Quit();
        return 1;
    }

    janela = SDL_CreateWindow(
        JANELA_NOME,
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        JANELA_LARGURA,
        JANELA_ALTURA,
        SDL_WINDOW_SHOWN
    );

    if (janela == NULL)
    {
        puts("Erro ao criar janela!");
        IMG_Quit();
        SDL_Quit();
        return 1;
    }

    tela = SDL_CreateRenderer(
        janela,
        -1,
        SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
    );

    if (tela == NULL)
    {
        puts("Erro ao criar tela renderizada!");
        SDL_DestroyWindow(janela);
        IMG_Quit();
        SDL_Quit();
        return 1;
    }

    if (carregar_texturas(tela, textura))
    {
        puts("Erro ao carregar texturas!");
        SDL_DestroyRenderer(tela);
        SDL_DestroyWindow(janela);
        IMG_Quit();
        SDL_Quit();
        return 1;
    }

    if (jogo_criar(&jogo, textura))
    {
        liberar_texturas(textura);
        SDL_DestroyRenderer(tela);
        SDL_DestroyWindow(janela);
        IMG_Quit();
        SDL_Quit();
        return 1;
    }

    while(loop)
    {
        while(SDL_PollEvent(&evento) != 0)
        {
            if (evento.type == SDL_QUIT) loop = 0;

            jogo_evento(&jogo, &evento);
        }

        SDL_SetRenderDrawColor(tela, JANELA_COR);
        SDL_RenderClear(tela);

        jogo_tela(&jogo, tela);

        SDL_RenderPresent(tela);

        SDL_Delay(JANELA_DELAY);
    }

    jogo_liberar(&jogo);
    liberar_texturas(textura);
    SDL_DestroyRenderer(tela);
    SDL_DestroyWindow(janela);
    IMG_Quit();
    SDL_Quit();

    return 0;
}