from grafo import Grafo
from vertice_aresta import Vertice, Aresta

class Fila:
    def __init__(self):
        self.l = []

    def insere(self, v: Vertice) -> None:
        self.l.append(v)

    def remove(self) -> Vertice:
        return self.l.pop(0) if len(self.l) > 0 else None

    def vazio(self) -> bool:
        return len(self.l) == 0

class Tempo:
    def __init__(self):
        self.tempo = 0

class Busca:
    def em_largura(g: Grafo, s: Vertice) -> dict:
        cores = dict()
        distancias = dict()
        arvore_busca = dict()
        for v in g.vertices:
            cores.update({v: 0})
            distancias.update({v: 0})
            arvore_busca.update({v: None})
        distancias[s] = 0
        cores[s] = 1
        Q = Fila()
        Q.insere(s)
        while not Q.vazio():
            u = Q.remove()
            for v in g.adj(u):
                if cores[v] == 0: # BRANCO
                    Q.insere(v)
                    cores[v] = 1 # CINZA
                    arvore_busca[v] = u
                    distancias[v] = distancias[u] + 1
            cores[u] = 2 # PRETO
        return arvore_busca

    def em_profundidade(g: Grafo, s: Vertice) -> dict:
        cores = dict()
        tempos_abertura = dict()
        tempos_fechamento = dict()
        arvore_busca = dict()
        for v in g.vertices:
            cores.update({v: 0})
            tempos_abertura.update({v: 0})
            tempos_fechamento.update({v: 0})
            arvore_busca.update({v: None})
        t = Tempo()

        def dfs_visit(u: Vertice):
            cores[u] = 1 # CINZA
            t.tempo += 1
            tempos_abertura[u] = t.tempo
            for v in g.adj(u):
                if cores[v] == 0: # BRANCO
                    arvore_busca[v] = u
                    dfs_visit(v)
            cores[u] = 2
            t.tempo += 1
            tempos_fechamento[u] = t.tempo

        for u in g.vertices:
            if cores[u] == 0: # BRANCO
                dfs_visit(u)
        return arvore_busca

def imprime_caminho(arvore_busca: dict, g: Grafo, s: Vertice, v: Vertice):
    if v == s:
        print(s)
    else:
        if arvore_busca[v] == None:
            print("Não há caminho de s para v")
        else:
            imprime_caminho(arvore_busca, g, s, arvore_busca[v])
            print(v)

def main():
    g = Grafo()
    g.cria_e_insere_v('v1')
    g.cria_e_insere_v('v2')
    g.cria_e_insere_v('v3')
    g.cria_e_insere_v('v4')
    g.cria_e_insere_v('v5')
    g.cria_e_insere_a('a1', g.vertices[0], g.vertices[1])
    g.cria_e_insere_a('a2', g.vertices[0], g.vertices[3])
    g.cria_e_insere_a('a3', g.vertices[1], g.vertices[3])
    g.cria_e_insere_a('a4', g.vertices[3], g.vertices[0])
    g.cria_e_insere_a('a5', g.vertices[3], g.vertices[4])
    g.cria_e_insere_a('a6', g.vertices[3], g.vertices[4])

    arvore_busca = Busca.em_largura(g, g.vertices[0])
    imprime_caminho(arvore_busca, g, g.vertices[0], g.vertices[4])

    # for key, value in Busca.em_profundidade(g, g.vertices[0]).items():
    #     print(key, value)

if __name__ == "__main__":
    main()