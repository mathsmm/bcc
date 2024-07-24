#include "App.h"

void App::OnEvent(SDL_Event event) 
{
	// Tipo de evento
	switch (event.type) 
	{
		// Tecla pressionada
		case SDL_KEYDOWN:
			switch (event.key.keysym.sym) 
			{
				// Escape (Esc)
				case SDLK_ESCAPE:
					running = false;
					break;

				default: break;
			}
			break;

		case SDL_QUIT:
			running = false;
			break;

		default: break;
	}
}