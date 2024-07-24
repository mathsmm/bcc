from Endereco import Endereco
from Pessoa import Pessoa


class Teste:

    def testarPessoaEndereco():
        pessoas_list   = []

        i = 1
        while True:
            in_nome = input(f"Informe o nome da pessoa {i} ('fim' para parar):")
            if in_nome.upper() == "FIM":
                break
            in_idade  = int(input(f"Informe a idade da pessoa {i}:"))
            in_rua    = input(f"Informe a rua do endereço da pessoa {i}:")
            in_numero = int(input(f"Informe o número do endereço da pessoa {i}:"))
            in_bairro = input(f"Informe o bairro do endereço da pessoa {i}:")
            in_cidade = input(f"Informe a cidade do endereço da pessoa {i}:")

            e = Endereco(in_rua, in_numero, in_bairro, in_cidade)
            p = Pessoa(in_nome, in_idade, e)
            pessoas_list.append(p)

            i += 1

        soma = 0
        maior_idade = pessoas_list[0].idade
        menor_idade = pessoas_list[0].idade
        for j in range(2, i):
            idade_pessoa_atual = pessoas_list[j].idade
            soma += idade_pessoa_atual
            if 
