from abc import ABC, abstractmethod
import random


# INTERFACE
class State(ABC):
    @abstractmethod
    def inserir_moeda(self):
        pass

    @abstractmethod
    def ejetar_moeda(self):
        pass

    @abstractmethod
    def virar_manivela(self):
        pass

    @abstractmethod
    def entregar(self):
        pass

class MaquinaBolinhas:
    def __init__(self, qtd_bolinhas: int) -> None:
        self.estoque = qtd_bolinhas
        self.est_sem_credito: State = SemCredito(self)
        self.est_com_credito: State = ComCredito(self)
        self.est_esgotado: State    = Esgotado(self)
        self.est_vendido: State     = Vendido(self)
        self.est_vencedor: State    = Vencedor(self)
        self.estado_atual: State    = self.est_sem_credito

# CONCRETAS
class SemCredito(State):
    def __init__(self, maquina: MaquinaBolinhas) -> None:
        self.maq: MaquinaBolinhas = maquina

    def inserir_moeda(self):
        if self.maq.estoque <= 0:
            self.maq.estado_atual = self.maq.est_esgotado
            print("Máquina sem bolinhas")
        else:
            self.maq.estado_atual = self.maq.est_com_credito
            print("Moeda inserida")

    def ejetar_moeda(self):
        print("Você não inseriu moeda")

    def virar_manivela(self):
        print("Você acionou a alavanca mas não inseriu moeda")

    def entregar(self):
        print("Você acionou a alavanca mas não inseriu moeda")

class ComCredito(State):
    def __init__(self, maquina: MaquinaBolinhas) -> None:
        self.maq: MaquinaBolinhas = maquina

    def inserir_moeda(self):
        print("Você não pode inserir outra moeda")

    def ejetar_moeda(self):
        print("Moeda devolvida")
        self.maq.estado_atual = self.maq.est_sem_credito

    def virar_manivela(self):
        i = random.randint(1, 10)
        if i == 1:
            self.maq.estado_atual = self.maq.est_vencedor
            print("Parabéns! Você ganhou uma bolinha extra")
        else:
            self.maq.estado_atual = self.maq.est_vendido
            print("Uma bolinha te espera")

    def entregar(self):
        print("Nenhuma bolinha foi entregue")

class Vendido(State):
    def __init__(self, maquina: MaquinaBolinhas) -> None:
        self.maq: MaquinaBolinhas = maquina

    def inserir_moeda(self):
        print("Por favor, espere")

    def ejetar_moeda(self):
        print("Você já acionou a alavanca")

    def virar_manivela(self):
        print("Acionar novamente a alavanca não lhe dará outra bolinha")

    def entregar(self):
        self.maq.estoque -= 1
        print("Bolinha fornecida")

        if self.maq.estoque <= 0:
            self.maq.estado_atual = self.maq.est_esgotado
        else:
            self.maq.estado_atual = self.maq.est_sem_credito

class Esgotado(State):
    def __init__(self, maquina: MaquinaBolinhas) -> None:
        self.maq: MaquinaBolinhas = maquina

    def inserir_moeda(self):
        print("Desculpe, mas a máquina está vazia")

    def ejetar_moeda(self):
        print("Você não inseriu moeda")

    def virar_manivela(self):
        print("Desculpe, mas a máquina está vazia")

    def entregar(self):
        print("Nenhuma bolinha foi fornecida")

class Vencedor(State):
    def __init__(self, maquina: MaquinaBolinhas) -> None:
        self.maq: MaquinaBolinhas = maquina

    def inserir_moeda(self):
        print("Por favor, espere")

    def ejetar_moeda(self):
        print("Você já acionou a alavanca")

    def virar_manivela(self):
        print("Acionar novamente a alavanca não lhe dará outra bolinha")

    def entregar(self):
        print("Bolinha fornecida")
        if self.maq.estoque > 1:
            self.maq.estoque -= 2
            print("Você teve sorte! Foram fornecidas duas bolinhas")
        else:
            self.maq.estoque -= 1
            print("Uma bolinha fornecida")

        self.maq.estado_atual = self.maq.est_sem_credito

print("Criando a máquina com 10 bolinhas")
maq = MaquinaBolinhas(10)
print("====================")

maq.estado_atual.inserir_moeda()
maq.estado_atual.virar_manivela()
maq.estado_atual.entregar()
print("====================")

maq.estado_atual.inserir_moeda()
maq.estado_atual.ejetar_moeda()
maq.estado_atual.virar_manivela()
maq.estado_atual.inserir_moeda()
maq.estado_atual.entregar()
maq.estado_atual.virar_manivela()
maq.estado_atual.entregar()