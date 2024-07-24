from vertice_aresta import Vertice, Aresta
from grafo import Grafo
from algoritmos_conexidade import FlorestaConjuntos

class Custo:
    def kruskal(g: Grafo):
        T = Grafo()
        f = FlorestaConjuntos()
        for v in g.vertices:
            f.cria_conjunto(v)
        arestas_ordenadas = g.a_ordenadas_custo()
        for a in arestas_ordenadas:
            if f.busca_conjunto(a.incid[0]) != f.busca_conjunto(a.incid[1]):
                f.uniao(a.incid[0], a.incid[1])
                u = T.get_v_por_id(a.incid[0].id)
                if u == None:
                    u = T.cria_e_insere_v(a.incid[0].id)
                v = T.get_v_por_id(a.incid[1].id)
                if v == None:
                    v = T.cria_e_insere_v(a.incid[1].id)
                T.cria_e_insere_a(a.id, u, v).custo = a.custo
        return T

def printar_vertices(g: Grafo):
    for vert in g.vertices:
        print(f"Adjacentes de {vert}:")
        for chave, valor in vert.adj.items():
            print(chave, end=": ")
            s = "["
            for a in valor:
                s += a.__str__() + ", "
            s = s[:-2]
            print(f"{s}]")

def main():
    g = Grafo()
    g.cria_e_insere_v('a')
    g.cria_e_insere_v('b')
    g.cria_e_insere_v('c')
    g.cria_e_insere_v('d')
    g.cria_e_insere_v('e')
    g.cria_e_insere_v('f')
    g.cria_e_insere_v('g')
    g.cria_e_insere_a('a1', g.vertices[0], g.vertices[1])
    g.arestas[0].custo = 14
    g.cria_e_insere_a('a2', g.vertices[0], g.vertices[3])
    g.arestas[1].custo = 4
    g.cria_e_insere_a('a3', g.vertices[0], g.vertices[4])
    g.arestas[2].custo = 3
    g.cria_e_insere_a('a4', g.vertices[1], g.vertices[2])
    g.arestas[3].custo = 10
    g.cria_e_insere_a('a5', g.vertices[1], g.vertices[3])
    g.arestas[4].custo = 8
    g.cria_e_insere_a('a6', g.vertices[1], g.vertices[6])
    g.arestas[5].custo = 2
    g.cria_e_insere_a('a6', g.vertices[2], g.vertices[6])
    g.arestas[6].custo = 13
    g.cria_e_insere_a('a6', g.vertices[3], g.vertices[4])
    g.arestas[7].custo = 9
    g.cria_e_insere_a('a6', g.vertices[3], g.vertices[5])
    g.arestas[8].custo = 2
    g.cria_e_insere_a('a6', g.vertices[3], g.vertices[6])
    g.arestas[9].custo = 6
    g.cria_e_insere_a('a6', g.vertices[4], g.vertices[5])
    g.arestas[10].custo = 8
    g.cria_e_insere_a('a6', g.vertices[5], g.vertices[6])
    g.arestas[11].custo = 8

    printar_vertices(Custo.kruskal(g))
    # printar_vertices(g)

if __name__ == "__main__":
    main()