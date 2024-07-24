#include "App.h"

void App::OnBeforeLoop()
{
	global.set_ticks(SDL_GetTicks());
	OnRenderClear();
	OnLoopThroughParticles();
	OnRenderPresent();
	OnTimeDelay();
	SDL_Delay((Uint32)2000);
}