#include "App.h"

void App::OnParticleMove(Particle& particle)
{
	// Posição no instante i + 1 = Posição no instante i + Velocidade * DT Real.
	particle.set_pos(particle.get_pos() + (particle.get_vel() * global.get_rDT()));
}