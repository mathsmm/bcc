from vertice_aresta import VerticeDirigido, ArestaDirigida

class Digrafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def get_ordem(self) -> int:
        return len(self.vertices)

    def get_tamanho(self) -> int:
        return len(self.arestas)

    def vertices(self) -> list:
        return self.vertices

    def arestas(self) -> list:
        return self.arestas

    # Inserção e remoção de vértices
    def insere_v(self, v: VerticeDirigido) -> VerticeDirigido:
        return self.vertices.append(v)

    def cria_e_insere_v(self, id: str) -> VerticeDirigido:
        v = VerticeDirigido(id)
        return self.insere_v(v)

    def remove_v(self, v: VerticeDirigido) -> VerticeDirigido:
        self.vertices.remove(v)
        for vert_suc in v.suc.keys():
            vert_suc.ant.pop(v)
        for vert_ant in v.ant.keys():
            vert_ant.suc.pop(v)
        for arestas_saida in v.suc.values():
            for aresta_saida in arestas_saida:
                self.arestas.remove(aresta_saida)
        for arestas_entrada in v.ant.values():
            for aresta_entrada in arestas_entrada:
                self.arestas.remove(aresta_entrada)
        return v

    # Inserção e remoção de arestas
    def insere_a(self, a: ArestaDirigida, u: VerticeDirigido, v: VerticeDirigido) -> ArestaDirigida:
        a.incid = (u, v)
        if (u in v.ant) or (v in u.suc):
            u.suc[v].append(a)
            v.ant[u].append(a)
        else:
            u.suc[v] = [a]
            v.ant[u] = [a]
        self.arestas.append(a)
        return a

    def cria_e_insere_a(self, id: str, u: VerticeDirigido, v: VerticeDirigido) -> ArestaDirigida:
        a = ArestaDirigida(id)
        return self.insere_a(a, u, v)

    def remove_a(self, a: ArestaDirigida) -> ArestaDirigida:
        self.arestas.remove(a)
        a.incid[0].suc[a.incid[1]].remove(a)
        if len(a.incid[0].suc[a.incid[1]]) == 0:
            a.incid[0].suc.pop(a.incid[1])
        a.incid[1].ant[a.incid[0]].remove(a)
        if len(a.incid[1].ant[a.incid[0]]) == 0:
            a.incid[1].ant.pop(a.incid[0])
        return a

    # Iterável de adjacência
    def adj(self, v: VerticeDirigido) -> set:
        return set(v.ant.keys()).union(set(v.suc.keys()))

    # Aresta a partir de dois vértices
    def get_a(self, u: VerticeDirigido, v: VerticeDirigido) -> list | None:
        if v in u.suc:
            return u.suc[v]
        elif u in v.ant:
            return u.ant[v]
        else:
            return None

    # Grau
    def grau_e(self, v: VerticeDirigido) -> int:
        grau = 0
        for arestas_entrada in v.ant.values():
            grau += len(arestas_entrada)
        return grau

    def grau_s(self, v: VerticeDirigido) -> int:
        grau = 0
        for arestas_saida in v.suc.values():
            grau += len(arestas_saida)
        return grau

    # Incidência
    def vertices_a(self, a: ArestaDirigida) -> tuple:
        return a.incid

    def oposto(self, v: VerticeDirigido, a: ArestaDirigida) -> VerticeDirigido:
        return a.incid[(a.incid.index(v) + 1) % 2]

def printar_vertices(g: Digrafo):
    for vert in g.vertices:
        print(f"\nSucessores de {vert}:")
        for chave, valor in vert.suc.items():
            print(chave, end=": ")
            s = "["
            for a in valor:
                s += a.__str__() + ", "
            s = s[:-2]
            print(f"{s}]")
        print(f"Antecessores de {vert}:")
        for chave, valor in vert.ant.items():
            print(chave, end=": ")
            s = "["
            for a in valor:
                s += a.__str__() + ", "
            s = s[:-2]
            print(f"{s}]")

def main():
    g = Digrafo()
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
    
    # Teste 1
    # for vert in g.vertices:
    #     print(vert)
    # for aresta in g.arestas:
    #     print(aresta) 

    # Teste 1.1
    # printar_vertices(g)

    # Teste 2
    # printar_vertices(g)
    # print('==================== REMOÇÃO DA ARESTA a3')
    # g.remove_a(g.arestas[2])
    # printar_vertices(g)
    # print('==================== REMOÇÃO DA ARESTA a6')
    # g.remove_a(g.arestas[4])
    # printar_vertices(g)
    # print('==================== REMOÇÃO DA ARESTA a5')
    # g.remove_a(g.arestas[3])
    # printar_vertices(g)

    # Teste 3
    # for aresta in g.arestas:
    #     print(aresta)
    # print('=================')
    # g.remove_v(g.vertices[1])
    # for aresta in g.arestas:
    #     print(aresta)

    # Teste 3.1
    # for aresta in g.arestas:
    #     print(aresta)
    # print('====================')
    # g.remove_v(g.vertices[3])
    # for aresta in g.arestas:
    #     print(aresta)

    # Teste 4
    # for vert_adj in g.adj(g.vertices[3]):
    #     print(vert_adj)
    # print('====================')
    # g.remove_a(g.arestas[2])
    # for vert_adj in g.adj(g.vertices[3]):
    #     print(vert_adj)

    # Teste 4.1
    # for vert_adj in g.adj(g.vertices[3]):
    #     print(vert_adj)
    # print('====================')
    # g.remove_a(g.arestas[5])
    # for vert_adj in g.adj(g.vertices[3]):
    #     print(vert_adj)

    # Teste 5
    # for v in g.vertices:
    #     print(g.grau_e(v))
    # print('====================')
    # g.remove_a(g.arestas[2])
    # for v in g.vertices:
    #     print(g.grau_e(v))

    # Teste 5.1
    # for v in g.vertices:
    #     print(g.grau_s(v))
    # print('====================')
    # g.remove_a(g.arestas[5])
    # for v in g.vertices:
    #     print(g.grau_s(v))

    # Teste 6
    # for a in g.get_a(g.vertices[0], g.vertices[3]):
    #     print(a)
    # for a in g.get_a(g.vertices[3], g.vertices[0]):
    #     print(a)

    # Teste 7
    # print(g.oposto(g.vertices[0], g.arestas[1]))
    # print(g.oposto(g.vertices[3], g.arestas[1]))

if __name__=='__main__':
    main()