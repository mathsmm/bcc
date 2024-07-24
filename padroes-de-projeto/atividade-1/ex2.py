from abc import ABC, abstractmethod


# Comp é Comportamento
class CompNavegacao(ABC):
    @abstractmethod
    def navegar(self):
        pass

class CompNavegaComMotor(CompNavegacao):
    def navegar(self):
        print("Navegando com motor.")

class CompNavegaComRemos(CompNavegacao):
    def navegar(self):
        print("Navegando com remos.")

class CompNavegaComVelas(CompNavegacao):
    def navegar(self):
        print("Navegando com velas.")


class Barco():
    def __init__(self) -> None:
        self.comp_navegacao: CompNavegacao = None

    def display(self):
        pass

    def efetuar_navegar(self):
        self.comp_navegacao.navegar()

    def set_comp_navegacao(self, comp_navegacao: CompNavegacao):
        self.comp_navegacao = comp_navegacao

class Bateira(Barco):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Mostrando barco Bateira")

class Iate(Barco):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Mostrando barco Iate")

class Canoa(Barco):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Mostrando barco Canoa")

class Jangada(Barco):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Mostrando barco Jangada")

class BarcoAVela(Barco):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Mostrando Barco à Vela")


def main():
    cn1 = CompNavegaComMotor()
    cn2 = CompNavegaComRemos()
    cn3 = CompNavegaComVelas()

    b1 = Bateira()
    b1.set_comp_navegacao(cn1)

    b2 = Iate()
    b2.set_comp_navegacao(cn1)

    b3 = Canoa()
    b3.set_comp_navegacao(cn2)

    b4 = Jangada()
    b4.set_comp_navegacao(cn2)

    b5 = BarcoAVela()
    b5.set_comp_navegacao(cn3)

    print("Comportamento da Bateira")
    print("efetuar_navegar: ", end="")
    b1.efetuar_navegar()
    print()

    print("Comportamento do Iate")
    print("efetuar_navegar: ", end="")
    b2.efetuar_navegar()
    print()

    print("Comportamento da Canoa")
    print("efetuar_navegar: ", end="")
    b3.efetuar_navegar()
    print()

    print("Comportamento da Jangada")
    print("efetuar_navegar: ", end="")
    b4.efetuar_navegar()
    print()

    print("Comportamento do Barco à Vela")
    print("efetuar_navegar: ", end="")
    b5.efetuar_navegar()
    print()


if __name__ == "__main__":
    main()