from Endereco import Endereco
from Pessoa import Pessoa


class Teste:
    def testarPessoaEndereco():
        ep1 = Endereco(
            "Pedro Benjamino de Oliveira",
            189,
            "Itoupava Central",
            "Blumenau"
        )
        p1 = Pessoa("Matheus", 22, ep1)
        print(p1.retornarDados())