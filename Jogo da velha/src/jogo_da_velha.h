#ifndef JOGO_DA_VELHA_H_INCLUDED
#define JOGO_DA_VELHA_H_INCLUDED

#define JANELA_NOME "Jogo da velha"
#define JANELA_LARGURA 300
#define JANELA_ALTURA 300
#define JANELA_COR 255, 255, 255, 255
#define JANELA_DELAY 30

#define TEXTURA_QUANTIDADE 2

enum Textura
{
    TEXTURA_X,
    TEXTURA_O
};

int carregar_texturas(SDL_Renderer *tela, SDL_Texture **textura);
void liberar_texturas(SDL_Texture **textura);

#endif