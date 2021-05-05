#ifndef JOGO_DA_VELHA_H_INCLUDED
#define JOGO_DA_VELHA_H_INCLUDED

#define JANELA_NOME "Jogo da velha"
#define JANELA_LARGURA 300
#define JANELA_ALTURA 300
#define JANELA_COR 200, 50, 100, 255
#define JANELA_DELAY 30

#define TEXTURA_QUANTIDADE 2

enum Textura
{
    TEXTURA_X,
    TEXTURA_O
};

static char *textura_arquivo[TEXTURA_QUANTIDADE] = {
    "../imagem/x.png",
    "../imagem/circulo.png"
};

int carregar_texturas(SDL_Renderer *tela, SDL_Texture **textura);
void liberar_texturas(SDL_Texture **textura);

#endif