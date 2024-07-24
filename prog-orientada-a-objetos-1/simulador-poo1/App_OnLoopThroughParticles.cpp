#include "App.h"

void App::OnLoopThroughParticles()
{
	int i = 0;
	int j = 0;
	int size = (int)global.vectorParticle.size();
	while (i < size)
	{
		OnParticleMove(global.vectorParticle[i]);
		OnParticleBorderCollision(global.vectorParticle[i]);

		j = 0;
		while (j < size)
		{
			// Não se pode verificar colisão de um círculo
			// com ele mesmo
			if (i == j)
			{
				j += 1;
				continue;
			}

			OnParticleCollision(global.vectorParticle[i], global.vectorParticle[j]);

			j += 1;
		}

		OnRenderParticle(global.vectorParticle[i]);

		i += 1;
	}
}