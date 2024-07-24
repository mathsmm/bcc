#include "App.h"

void App::OnRenderPresent()
{
	//Atualiza a janela com o renderizador
	SDL_RenderPresent(renderer);
}