#include "App.h"

void App::OnParticleBorderCollision(Particle& particle)
{
	bool verticalCollision = false;

	// Lateral esquerda
	if (particle.get_pos().get_x() - particle.get_rad() <= 0)
	{
		verticalCollision = true;

		particle.set_pos(
			Vect(
				particle.get_rad() + 1,
				particle.get_pos().get_y()
			)
		);

		particle.set_vel(
			Vect(
				particle.get_vel().get_x() * -1,
				particle.get_vel().get_y()
			)
		);
	}

	// Lateral direita
	if (!verticalCollision && particle.get_pos().get_x() + particle.get_rad() >= global.get_width())
	{
		particle.set_pos(
			Vect(
				global.get_width() - particle.get_rad() - 1,
				particle.get_pos().get_y()
			)
		);

		particle.set_vel(
			Vect(
				particle.get_vel().get_x() * -1,
				particle.get_vel().get_y()
			)
		);
	}

	bool horizontalCollision = false;

	// Cima
	if (particle.get_pos().get_y() - particle.get_rad() <= 0)
	{
		horizontalCollision = true;

		particle.set_pos(
			Vect(
				particle.get_pos().get_x(),
				particle.get_rad() + 1
			)
		);

		particle.set_vel(
			Vect(
				particle.get_vel().get_x(),
				particle.get_vel().get_y() * -1
			)
		);
	}

	// Baixo
	if (!horizontalCollision && particle.get_pos().get_y() + particle.get_rad() >= global.get_heigth())
	{
		particle.set_pos(
			Vect(
				particle.get_pos().get_x(),
				global.get_heigth() - particle.get_rad() - 1
			)
		);

		particle.set_vel(
			Vect(
				particle.get_vel().get_x(),
				particle.get_vel().get_y() * -1
			)
		);
	}
}