arquivo = open('caminho_do_arquivo', 'r')
"""
O primeiro parâmetro é o nome do arquivo que queremos
ler e com o segundo parâmetro, atribuído ao valor “r”, afirmamos que queremos ler do arquivo.
O “r” é opcional. Um comando open com apenas um nome de arquivo é aberto para leitura por
padrão. A função open retorna um objeto de arquivo, que oferece métodos e atributos de arquivo.
"""

arquivo.close()
"""
Depois de termos finalizado o trabalho com um arquivo, devemos fechá-lo novamente usando o
método do objeto do arquivo close:
"""

arquivo = open ("/Users/rodacki/Developer/files/poemafp.txt", "r")
for line in arquivo :
    pass
# print(line . rstrip())
arquivo.close()
"""
Agora vamos finalmente abrir e ler os dados contidos em um arquivo. O método rstrip no exemplo
acima é usado para retirar os espaços em branco (incluindo o caracter de nova linha ou newline)
do lado direito da string “line”:
"""


"""
O seguinte código abre um objeto de arquivo de escrita em um arquivo chamado “files/myfile.txt”.
Se o arquivo não existir, ele será criado com o nome do caminho fornecido. Se o arquivo já existe,
o Python o abre. Quando os dados são gravados no arquivo e o arquivo é fechado (close), todos
os dados anteriormente existentes no arquivo são apagados. Os dados de sequência de caracteres
(strings) são escritos (ou gravados) para um arquivo usando o método de gravação com o objeto de
arquivo. O método de escrita espera um único argumento de string. Se você quiser que o texto de
saída termine com uma nova linha, você deve incluir o caractere de escape \n na string. O exemplo
a seguir escreve duas linhas de texto no arquivo:
"""
f = open("/Users/rodacki/Developer/files/myfile.txt", 'w')
f.write("First line.\nSecond line.\n")
f.close()
#Saída (conteúdo do arquivo):
# First line.
# Second line.


"""
O próximo trecho de código ilustra a saída de inteiros para um arquivo texto. Cinco números inteiros
aleatórios entre 1 e 500 são gerados e escritos em um arquivo texto chamado “files/integers.txt”.
O caractere de newline é o separador.
"""
import random
# 14.1. ARQUIVOS TEXTO 115
f = open("/Users/rodacki/Developer/files/integers.txt", 'w')
for count in range (5):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")
f.close()
# Saída (conteúdo do arquivo):
# 278
# 205
# 213
# 162
# 285


"""
Lendo dados de um arquivo texto
"""
f =open("/Users/rodacki/Developer/files/integers.txt", 'r')
text = f.read()
print(text)


"""
uma aplica¸c˜ao pode ler e processar o texto, uma linha de cada vez. Um la¸co
for cumpre isso muito bem. O la¸co for exibe um objeto de arquivo como uma sequ¨ˆencia de linhas
de texto. Em cada itera¸c˜ao do la¸co, a vari´avel de itera¸c˜ao est´a vinculada `a pr´oxima linha de texto
na sequ¨ˆencia. No exemplo a seguir, reabrimos o nosso arquivo de exemplo e visitamos as linhas de
texto nele contidas:
"""
f = open("/Users/rodacki/Developer/files/integers.txt", 'r')
l = 1
for line in f:
    print("Linha", l, line.rstrip())
    l = l + 1
f.close()
# Saída:
# Linha 1 278
# Linha 2 205
# Linha 3 213
# Linha 4 162
# Linha 5 285


"""
O tratamento de exceções é particularmente útil ao trabalhar com a entrada do usuário, ou ao ler
ou escrever para arquivos, porque tais interações são inerentemente menos previsíveis. Num
exemplo para arquivo inexistente podemos fazer:
"""
try:
    arq = open("files/naoExiste.txt", "r")
    print("Arquivo aberto com sucesso.")
except FileNotFoundError :
    print("Não foi possível abrir o arquivo.")
print ("Fim")


"""
O exemplo abaixo lê um arquivo e mostra o conteúdo dele na tela
"""
try :
    arq = open("/Users/rodacki/Developer/files/versos.txt", "r")
    while True:
        s = arq.read(1)
        print(s, end ="")
        if(s == ""):
            break
    arq.close()
except:
    print("Arquivo versos.txt não pôde ser aberto.")

"""
Com o modo de operação “r+” (ver tabela abaixo), podemos ler todo o texto de um arquivo e fazer
qualquer alteração que julgarmos necessária. O texto alterado pode então ser sobrescrito sobre o
texto anterior. Ao realizar a leitura de um caractere, ou uma linha, automaticamente o indicador
de posição do arquivo se move para o próximo caractere (ou linha). Para voltar ao início do arquivo
novamente você pode usar o método seek:
seek(offset, from_what)
onde o primeiro parâmetro indica quantos bytes se mover a partir do valor inicial from what. Os
valores de from what podem ser: 0: indica início do arquivo. 1: indica a posição atual no arquivo.
2: indica a posição final do arquivo.

Os modos de abertura de arquivo texto e o indicador de posição são:
---------------------------------------------------
| modo | operações         | indicador de posição |
| ------------------------------------------------|
| r    | leitura           | início do arquivo    |
| r+   | leitura e escrita | início do arquivo    |
| w    | escrita           | início do arquivo    |
| a    | (append) escrita  | final do arquivo     |
---------------------------------------------------
"""