from math import sin, cos, asin, acos, pi


def degree_to_rad(degree: float):
    return (degree * pi) / 180

class Vect:
    def __init__(
        self, 
        coordinate_x: float,
        coordinate_y: float) -> None:
        """
        Inicia um objeto do tipo Vect que representa um vetor
        bidimensional a partir do ponto O(0, 0), a origem.\n
        Os argumentos são coordenadas x e y.
        """
        self.x = coordinate_x
        self.y = coordinate_y

    def __str__(self):
        return f"<{self.x},{self.y}>"

    # Redefine o operador de adição
    def __add__(self, v):
        if isinstance (v, Vect):
            return Vect(self.x + v.x, self.y + v.y)

    # Redefine o operador de subtração
    def __sub__(self, v):
        if isinstance (v, Vect):
            return Vect(self.x - v.x, self.y - v.y)

    # Redefine o operador de multiplicação
    def __mul__(self, v):
        if isinstance (v, Vect):
            return Vect(self.x * v.x, self.y * v.y)
        if isinstance (v, float):  
            return Vect(self.x * v, self.y * v)

    def module(self):
        """
        Retorna o módulo (distância) entre a origem O(0, 0)
        e o ponto que representa o vetor.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def vsin(self):
        """Retorna o seno do ângulo do vetor"""
        return self.y / self.module()

    def vcos(self):
        """Retorna o cosseno do ângulo do vetor"""
        return self.x / self.module()

    def alpha(self):
        """
        Retorna o ângulo em radianos do vetor em relação
        à parte positiva do eixo x.\n
        O valor de retorno está entre 0 e 2pi
        """
        vsin = self.vsin()
        vcos = self.vcos()
        if vsin < 0:                   # 1º e 2º quadrantes
            return 2 * pi - acos(vcos)
        elif vsin > 0:                 # 3º e 4º quadrantes
            return acos(vcos)
        elif vsin == 0 and vcos == 1:  # 0°
            return 0
        elif vsin == 0 and vcos == -1: # 180°
            return pi

        # if   vsin > 0 and vcos > 0: # 1º Quadrante
        #     return asin(vsin)
        # elif vsin > 0 and vcos < 0: # 2º Quadrante
        #     return pi - asin(vsin)
        # elif vsin < 0 and vcos < 0: # 3º Quadrante
        #     return pi - asin(vsin)
        # elif vsin < 0 and vcos > 0: # 4º Quadrante
        #     return 2 * pi + asin(vsin)

        # if   vsin > 0 and vcos > 0: # 1º Quadrante
        #     return acos(vcos)
        # elif vsin > 0 and vcos < 0: # 2º Quadrante
        #     return acos(vcos)
        # elif vsin < 0 and vcos < 0: # 3º Quadrante
        #     return 2 * pi - acos(vcos)
        # elif vsin < 0 and vcos > 0: # 4º Quadrante
        #     return 2 * pi - acos(vcos)

    def inc_alpha(self, rad_inc: float):
        """
        Altera as coordenadas (x, y) do vetor de modo a incrementar
        seu ângulo a partir de um dado valor em radiano.
        """
        module = self.module()
        incremented_alpha = self.alpha() + rad_inc
        self.x = module * cos(incremented_alpha)
        self.y = module * sin(incremented_alpha)


def main():
    # v1 = Vect(1, 2)
    # print(v1)
    pass

if __name__ == "__main__":
    main()