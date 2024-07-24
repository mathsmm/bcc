#include "App.h"

void App::OnTimeDelay()
{
	// dT recebe a diferença de ticks entre o começo da
	// execução do laço e o final
	global.set_dT(SDL_GetTicks() - global.get_ticks());

	if (global.get_dT() < global.get_dDT())
	{
		// Pausa a execução por um tempo para o FPS atingir
		// valores próximos ao desejado
		SDL_Delay((Uint32)(global.get_dDT() - global.get_dT()));
	}

	// Mostra o FPS atual
	//SDL_Log("FPS: %i", 1000 / (SDL_GetTicks() - global.get_ticks()));

	// rDT recebe a diferença REAL de ticks entre o começo
	// da execução do laço e o final. (O tempo de execução 
	// deste método também é relevante!)
	global.set_rDT((SDL_GetTicks() - global.get_ticks()) / 1000.0);
}