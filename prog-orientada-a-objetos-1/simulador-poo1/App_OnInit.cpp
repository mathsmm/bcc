#include "App.h"

void App::OnInit()
{
	global = AppVar(60, 800, 600, 24, LoadFromArchive("particulas.txt"));

	if (SDL_Init(SDL_INIT_EVERYTHING) < 0) 
	{
		SDL_Log("SDL não pôde ser inicializado: ", SDL_GetError());
		exit(1);
	}

	window = SDL_CreateWindow(
		"Simulador",
		SDL_WINDOWPOS_UNDEFINED,
		SDL_WINDOWPOS_UNDEFINED,
		global.get_width(),
		global.get_heigth(),
		SDL_WINDOW_RESIZABLE | SDL_WINDOW_OPENGL
	);

	renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

	if (window == NULL) 
	{
		SDL_Log("A janela SDL está com valor nulo. Erro: ", SDL_GetError());
		exit(1);
	}

	if (renderer == NULL)
	{
		SDL_Log("O renderizador SDL está com valor nulo. Erro: ", SDL_GetError());
		exit(1);
	}
}
