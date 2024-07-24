/*****************************************************************//**
 * \file   Particle.h
 * \brief  
 * 
 * \date   October 2022
 *********************************************************************/

#pragma once
#include "Body.h"
#include "Vect.h"
#include <vector>

class Particle : public Body
/** Classe que representa uma partícula circular. */
{
	private:
		// Raio da partícula (a partícula é circular)
		double radius;

	public:
		// Construtor padrão.
		Particle();

		/**
		 * Construtor. Inicializa uma partícula.
		 * 
		 * \param initialPosition Vetor de posição inicial
		 * \param initalVelocity Vetor de velocidade inicial
		 * \param radius Raio
		 */
		Particle(Vect initialPosition, Vect initalVelocity, double radius);

		double get_rad();

		static std::vector<Particle> createVectorParticle1();
		static std::vector<Particle> createVectorParticle2();
		static std::vector<Particle> createVectorParticle3();
		static std::vector<Particle> createVectorParticle4();
};