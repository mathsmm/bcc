class Vertice:
    def __init__(self, id: str):
        self.id = id
        self.adj = dict() # Adjacentes

    def __str__(self):
        return f'<{self.id}>'

class Aresta:
    def __init__(self, id: str):
        self.id = id
        self.incid = tuple()
        self.custo = 1

    def __str__(self):
        return f'<({self.incid[0].id} -- {self.incid[1].id}) {self.id}>'

class VerticeDirigido:
    def __init__(self, id: str):
        self.id = id
        self.suc = dict() # Sucessores
        self.ant = dict() # Antecessores

    def __str__(self):
        return f'<{self.id}>'

class ArestaDirigida:
    def __init__(self, id: str):
        self.id = id
        self.incid = tuple()

    def __str__(self):
        return f'<({self.incid[0].id} -> {self.incid[1].id}) {self.id}>'