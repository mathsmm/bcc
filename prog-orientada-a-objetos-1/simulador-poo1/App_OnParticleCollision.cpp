#include "App.h"
#include "AppUtils.h"

void App::OnParticleCollision(Particle& particle1, Particle& particle2)
{
	// Se o produto escalar entre o vetor formado pelos vetores de posição
	// e o vetor formado pelos vetores de velocidade for maior ou igual
	// a zero, as partículas não estão se aproximando
	if (Vect(particle1.get_pos(), particle2.get_pos()) *
		Vect(particle1.get_vel(), particle2.get_vel()) >= 0)
	{
		return;
	}

	// Se a soma dos raios das partículas for menor que a distância 
	// entre as posições das partículas, não há colisão
	if (particle1.get_rad() + particle2.get_rad() <
		AppUtils::s_DistanceBetweenParticles(particle1, particle2))
	{
		SDL_Log("Não vou colidir");
		return;
	}

	SDL_Log("Colisão!");

	// Para maiores esclarecimentos,
	// https://www.vobarian.com/collisions/2dcollisions2.pdf
	// Este PDF também está na pasta "Utilidades" deste repositório

	// Acrônimos:
	// v  -> Vetor
	// uV -> Vetor unitário
	// 1  -> Referente à partícula 1
	// 2  -> Referente à partícula 2
	// N  -> Normal (perpendicular)
	// T  -> Tangente
	// B  -> Before collision (Antes da colisão)
	// A  -> After collision (Depois da colisão)
	// c  -> Componente (grandeza escalar)
	// m  -> Massa

	// Passo 1 - Achar vetor unitário normal e vetor unitário tangente.
	// Eles formam "eixos" que serão utilizados em passos seguintes

	// "Eixo y"
	Vect uVN = Vect(particle1.get_pos(), particle2.get_pos()).unitVect();
	
	// "Eixo x"
	Vect uVT = Vect(-uVN.get_y(), uVN.get_x());

	// Passo 2 - Criar os vetores de velocidade inicial 
	// (antes da colisão) de ambos os círculos. 
	// OBS: Eles já existem (objParticle.getVel())

	// Passo 3 - Projetar os vetores de velocidade inicial
	// nos vetores unitários normal e tangente.
	// Isto pode ser feito ao efetuar o produto escalar entre
	// os vetores unitários e os vetores de velocidade
	double v1NBc = uVN * particle1.get_vel();
	double v1TBc = uVT * particle1.get_vel();
	double v2NBc = uVN * particle2.get_vel();
	double v2TBc = uVT * particle2.get_vel();

	// Passo 4 - Encontrar as velocidades tangenciais
	// pós-colisão. Elas são iguais às pré-colisão
	double v1TAc = v1TBc;
	double v2TAc = v2TBc;

	// Passo 5 - Encontrar as velocidades normais
	// pós-colisão. Utiliza-se as fórmulas de momento
	// e de energia cinética em uma dimensão
	double m1 = particle1.get_mass();
	double m2 = particle2.get_mass();
	double v1NAc = (v1NBc * (m1 - m2) + 2 * m2 * v2NBc) / (m1 + m2);
	double v2NAc = (v2NBc * (m2 - m1) + 2 * m1 * v1NBc) / (m1 + m2);

	// Passo 6 - Converter componentes normais e 
	// tangenciais em vetores
	Vect v1NA = uVN * v1NAc;
	Vect v1TA = uVT * v1TAc;
	Vect v2NA = uVN * v2NAc;
	Vect v2TA = uVT * v2TAc;

	// Passo 7 - Encontrar os vetores de velocidade
	// pós-colisão e aplicá-los às partículas
	particle1.set_vel(v1NA + v1TA);
	particle2.set_vel(v2NA + v2TA);
}