class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []

    def agregar_nodo(self, nodo_id, informacion):
        self.nodos[nodo_id] = informacion

    def agregar_arista(self, origen, destino, peso):
        self.aristas.append((origen, destino, peso))
