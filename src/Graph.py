class Grafo_Dirigido:
    
    def __init__(self):
        self.grafo_dict = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo_dict:
            self.grafo_dict[vertice] = []
        else:
            return "El vertex ya existe"

    def agregar_arista(self, origen, destino, peso):
        self.aristas.append((origen, destino, peso))
