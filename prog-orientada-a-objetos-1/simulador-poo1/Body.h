#pragma once
#include "Vect.h"
class Body
{
	protected:
		// Vetor de posição
		Vect position;

		// Vetor de velocidade
		Vect velocity;

		//Vect acceleration;

		// Área
		double area;

		// Massa
		double mass;

		//double density;

	public:
		// Construtor padrão.
		Body();

		/**
		 * Construtor. Inicializa uma partícula.
		 *
		 * \param initialPosition Vetor de posição inicial
		 * \param initalVelocity Vetor de velocidade inicial
		 * \param area Área
		 */
		Body(Vect initialPosition, Vect initalVelocity, double area);

		Vect get_pos();
		void set_pos(Vect pos);

		Vect get_vel();
		void set_vel(Vect newVel);

		double get_area();
		double get_mass();
};

