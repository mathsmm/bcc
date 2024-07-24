from Endereco import Endereco


class Pessoa:

    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.__nome  = nome
        self.__idade = idade
        self.__endereco = endereco

    #Properties
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def endereco(self):
        return self.__endereco

    #Setters
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @endereco.setter
    def endereco(self, endereco: Endereco):
        self.__endereco = endereco

    def retornarDados(self):
        return (
            "Nome:\t"   + f"{self.nome}\n"            +
            "Idade:\t"  + f"{self.idade}\n"           +
            "Rua:\t"    + f"{self.endereco.rua}\n"    +
            "Número:\t" + f"{self.endereco.numero}\n" +
            "Bairro:\t" + f"{self.endereco.bairro}\n" +
            "Cidade:\t" + f"{self.endereco.cidade}\n"
        )