from random import randint
from names import get_full_name
import sqlite3
from time import time
import os
import subprocess


def criar_e_popular_scripts():
    for i in range(1, 5):
        print(f"Criando e populando os scripts com 10^{i} + 2 registros")

        if os.path.isfile(f"script_varias_transacoes_{i}.sql") or os.path.isfile(f"script_transacao_unica_{i}.sql"):
            print("Já existe")
            continue

        startTime = 0.0
        startTime = time()

        lis = ["create table pessoa (id integer primary key, nome text, idade integer, salario integer);"]
        lis.append("insert into pessoa(id, nome, idade, salario) values ")

        x = (10**i)
        p = 0

        lis.append("(" + str(x + 1) + ", 'John TESTE', " + str(randint(1,100)) + ", " + str(randint(1, 100000)) + "), ")
        lis.append("(" + str(x + 2) + ", 'TESTE John', " + str(randint(1,100)) + ", " + str(randint(1, 100000)) + "), ")

        while x:
            if x % (10**(i-2)) == 0:
                p += 1
                print(f"{p}%" , end="\r")

            lis.append("(" + str(x) + ", " + "'" + get_full_name() + "'" \
            + ", " + str(randint(1,100)) + ", " + str(randint(1, 100000)) \
            + ")" + ", ")

            x -= 1

        try:
            script_v_t = open(f"script_varias_transacoes_{i}.sql", "w")
        except Exception as e:
            print(f"Não foi possível abrir o script_varias_transacoes_{i}. Mensagem de erro:\n {e}")

        script_v_t.write(lis[0] + "\n\n")
        for j in range(2, (10**i) + 2):
            script_v_t.write("BEGIN TRANSACTION;\n")
            script_v_t.write(lis[1] + lis[j][:-2] + ";\n")
            script_v_t.write("COMMIT;\n\n")
        script_v_t.close()

        lis[-1] = lis[-1][:-2] + ";"

        try:
            script_t_u = open(f"script_transacao_unica_{i}.sql", "w")
        except Exception as e:
            print(f"Não foi possível abrir o script_transacao_unica_{i}.sql. Mensagem de erro:\n {e}")
        script_t_u.write("\n".join(lis))
        script_t_u.close()

        print("Finalizado")
        print("Tempo em segundos: ", time() - startTime)
        print("--------------------------------------------------")

def executar_scripts():
    for i in range(1, 5):
        conn = sqlite3.connect(f"banco{i}.db")

        print(f"Executando o script_transacao_unica_{i}.sql no banco{i}.db")
        startTime = 0.0
        startTime = time()
        subprocess.run(["sqlite3", f"banco{i}.db", f".read script_transacao_unica_{i}.sql"])
        print("Tempo em segundos: ", time() - startTime)

        conn.cursor().execute("DROP TABLE pessoa")
        conn.commit()

        print(f"Executando o script_varias_transacoes_{i}.sql no banco{i}.db")
        startTime = 0.0
        startTime = time()
        subprocess.run(["sqlite3", f"banco{i}.db", f".read script_varias_transacoes_{i}.sql"])
        print("Tempo em segundos: ", time() - startTime)

        conn.commit()
        conn.close()

        print("Finalizado")
        print("--------------------------------------------------")

def fazer_selects():
    for i in range(1, 5):
        conn = sqlite3.connect(f"banco{i}.db")

        print(f"FAZENDO O SELECT COM WHERE NA FORMA nome LIKE '%John%' (banco{i}.db)")
        startTime = 0.0
        startTime = time()
        subprocess.run(["sqlite3", f"banco{i}.db", "SELECT * FROM pessoa WHERE nome LIKE '%John%'"], stdout=subprocess.DEVNULL)
        # conn.cursor().execute("SELECT * FROM pessoa WHERE nome LIKE '%John%'")
        conn.commit()
        print("Tempo em segundos: ", time() - startTime)

        print(f"FAZENDO O SELECT COM WHERE NA FORMA nome LIKE '%John' or 'John%' (banco{i}.db)")
        startTime = 0.0
        startTime = time()
        subprocess.run(["sqlite3", f"banco{i}.db", "SELECT * FROM pessoa WHERE nome LIKE '%John' or 'John%'"], stdout=subprocess.DEVNULL)
        # conn.cursor().execute("SELECT * FROM pessoa WHERE nome LIKE '%John' or 'John%'")
        conn.commit()
        print("Tempo em segundos:", time() - startTime)
        conn.close()

        print("--------------------------------------------------")


def main():
    print("--------------------------------------------------")
    print("CRIANDO SCRIPTS PARA INSERIR REGISTROS NOS BANCOS")
    print("--------------------------------------------------")
    criar_e_popular_scripts()
    print("--------------------------------------------------")
    print("TESTANDO INSERTS COM UMA ÚNICA TRANSAÇÃO E INSERTS EM TRANSAÇÕES DIFERENTES")
    print("--------------------------------------------------")
    executar_scripts()
    print("--------------------------------------------------")
    print(r"TESTANDO SELECTS COM CARACTERES CORINGA DOS DOIS LADOS E SELECTS NA FORMA ('%X' or 'X%')")
    print("--------------------------------------------------")
    fazer_selects()

if __name__ == '__main__':
    main()