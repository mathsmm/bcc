class Endereco:

    def __init__(self, rua: str, numero: int, bairro: str, cidade: str) -> None:
        self.__rua    = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade

    #Propriedade rua
    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua: str):
        self.__rua = rua

    #Propriedade numero
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    #Propriedade bairro
    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro

    #Propriedade cidade
    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    def retornarDados(self):
        return (
            f"Rua: {self.rua}\n" +
            f"Número: {self.numero}\n" +
            f"Bairro: {self.bairro}\n" +
            f"Cidade: {self.cidade}\n"
        )
