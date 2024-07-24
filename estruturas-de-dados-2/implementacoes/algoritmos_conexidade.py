from vertice_aresta import Vertice, Aresta
from grafo import Grafo

class FlorestaConjuntos:
    def __init__(self):
        self.arvore = dict()
        self.pesos = dict()

    def cria_conjunto(self, v: Vertice):
        self.arvore[v] = v
        self.pesos[v] = 0

    def busca_conjunto(self, v: Vertice):
        if v != self.arvore[v]:
            self.arvore[v] = self.busca_conjunto(self.arvore[v])
        return self.arvore[v]

    def link(self, u: Vertice, v: Vertice):
        if self.pesos[u] > self.pesos[v]:
            self.arvore[v] = u
        else:
            self.arvore[u] = v
            if self.pesos[u] == self.pesos[v]:
                self.pesos[v] += 1

    def uniao(self, u: Vertice, v: Vertice):
        self.link(self.busca_conjunto(u), self.busca_conjunto(v))

class Conexidade:
    def componentes_conexas_conjuntos(g: Grafo):
        f = FlorestaConjuntos()
        for v in g.vertices:
            f.cria_conjunto(v)
        for a in g.arestas:
            if f.busca_conjunto(a.incid[0]) != f.busca_conjunto(a.incid[1]):
                f.uniao(a.incid[0], a.incid[1])
        return f.arvore

def main():
    g = Grafo()
    g.cria_e_insere_v('a')
    g.cria_e_insere_v('b')
    g.cria_e_insere_v('c')
    g.cria_e_insere_v('d')
    g.cria_e_insere_v('e')
    g.cria_e_insere_v('f')
    g.cria_e_insere_v('g')
    g.cria_e_insere_v('h')
    g.cria_e_insere_v('i')
    g.cria_e_insere_v('j')
    g.cria_e_insere_a('a1', g.vertices[0], g.vertices[5])
    g.cria_e_insere_a('a2', g.vertices[1], g.vertices[6])
    g.cria_e_insere_a('a3', g.vertices[3], g.vertices[8])
    g.cria_e_insere_a('a4', g.vertices[4], g.vertices[8])
    g.cria_e_insere_a('a5', g.vertices[4], g.vertices[9])
    g.cria_e_insere_a('a6', g.vertices[6], g.vertices[7])
    g.cria_e_insere_a('a7', g.vertices[8], g.vertices[9])

    for k, v in Conexidade.componentes_conexas_conjuntos(g).items():
        print(k, ":", v)

if __name__ == "__main__":
    main()