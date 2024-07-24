from abc import ABC, abstractmethod


# Comp é Comportamento
class DefinirValorComportamento(ABC):
    @abstractmethod
    def definir_valor(self, comodos, espaco, localizacao) -> float:
        pass

class DefinirValorComEdificacao(DefinirValorComportamento):
    def definir_valor(self, comodos, espaco, localizacao):
        if localizacao == 'A':
            return (espaco * 3000) + (comodos * 1000)
        elif localizacao == 'B':
            return (espaco * 1000) + (comodos * 1000)
        elif localizacao == 'C':
            return (espaco * 500) + (comodos * 1000)

class DefinirValorSemEdificacao(DefinirValorComportamento):
    def definir_valor(self, comodos, espaco, localizacao):
        if localizacao == 'A':
            return (espaco * 1500)
        elif localizacao == 'B':
            return (espaco * 750)
        elif localizacao == 'C':
            return (espaco * 200)


class Imovel(ABC):
    def __init__(self, comodos, espaco, localizacao) -> None:
        self.__comodos = comodos
        self.__espaco = espaco
        self.__localizacao = localizacao

        self.__definir_valor_comp: DefinirValorComportamento = None

    def definir_valor(self):
        return self.__definir_valor_comp.definir_valor(self.__comodos, self.__espaco, self.__localizacao)

    def set_definir_valor(self, definir_valor_comp: DefinirValorComportamento):
        self.__definir_valor_comp = definir_valor_comp

    def get_comodos(self):
        return self.__comodos

    def get_espaco(self):
        return self.__espaco

    def get_localizacao(self):
        return self.__localizacao

class Casa(Imovel):
    def __init__(self, comodos, espaco, localizacao) -> None:
        super().__init__(comodos, espaco, localizacao)

class Apartamento(Imovel):
    def __init__(self, comodos, espaco, localizacao) -> None:
        super().__init__(comodos, espaco, localizacao)

class Terreno(Imovel):
    def __init__(self, comodos, espaco, localizacao) -> None:
        super().__init__(comodos, espaco, localizacao)

def main():
    dv1 = DefinirValorComEdificacao()
    dv2 = DefinirValorSemEdificacao()

    i1 = Casa(5, 100, 'A')
    i1.set_definir_valor(dv1)

    i2 = Casa(8, 150, 'C')
    i2.set_definir_valor(dv1)

    i3 = Apartamento(4, 35, 'B')
    i3.set_definir_valor(dv1)

    i4 = Apartamento(8, 200, 'A')
    i4.set_definir_valor(dv1)

    i5 = Terreno(0, 500, 'B')
    i5.set_definir_valor(dv2)

    i6 = Terreno(0, 1000, 'C')
    i6.set_definir_valor(dv2)

    print(f"Casa 1: {i1.get_comodos()} cômodos, {i1.get_espaco()}m2, localização {i1.get_localizacao()}")
    print(f"definir_valor: {i1.definir_valor()}")
    print()

    print(f"Casa 2: {i2.get_comodos()} cômodos, {i2.get_espaco()}m2, localização {i2.get_localizacao()}")
    print(f"definir_valor: {i2.definir_valor()}")
    print()

    print(f"Apartamento 1: {i3.get_comodos()} cômodos, {i3.get_espaco()}m2, localização {i3.get_localizacao()}")
    print(f"definir_valor: {i3.definir_valor()}")
    print()

    print(f"Apartamento 2: {i4.get_comodos()} cômodos, {i4.get_espaco()}m2, localização {i4.get_localizacao()}")
    print(f"definir_valor: {i4.definir_valor()}")
    print()

    print(f"Terreno 1: {i5.get_comodos()} cômodos, {i5.get_espaco()}m2, localização {i5.get_localizacao()}")
    print(f"definir_valor: {i5.definir_valor()}")
    print()

    print(f"Terreno 2: {i6.get_comodos()} cômodos, {i6.get_espaco()}m2, localização {i6.get_localizacao()}")
    print(f"definir_valor: {i6.definir_valor()}")
    print()

if __name__ == "__main__":
    main()