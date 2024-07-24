#include "App.h"

void App::OnCleanup() 
{
	SDL_DestroyWindow(window);
	SDL_Quit();
}
