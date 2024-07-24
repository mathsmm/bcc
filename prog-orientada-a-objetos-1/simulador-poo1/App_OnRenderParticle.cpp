#include "App.h"
#include "AppUtils.h"

void App::OnRenderParticle(Particle particle) 
{
	SDL_SetRenderDrawColor(renderer, 64, 128, 255, SDL_ALPHA_OPAQUE);

	// Desenha a partícula
	AppUtils::s_DrawParticle(
		renderer,
		particle,
		global.get_particleVertexQuantity()
	);

	SDL_SetRenderDrawColor(renderer, 255, 255, 0, SDL_ALPHA_OPAQUE);

	// Desenha o vetor de velocidade da partícula
	AppUtils::s_DrawVect(
		renderer,
		particle.get_pos(),
		particle.get_pos() + particle.get_vel()
	);

	//SDL_Rect rect = { 100,100,440,280 };
	//SDL_FillRect(Main_Surface, &rect, SDL_MapRGB(Main_Surface->format, 255, 0, 0));
	//SDL_UpdateWindowSurface(Window);
	//SDL_RenderDrawRect(Renderer, &rect);
}