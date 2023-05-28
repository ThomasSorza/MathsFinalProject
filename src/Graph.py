import Vertex
import Edge

class Grafo_Dirigido:
    """
    Clase que representa un grafo dirigido. Se utiliza un diccionario 
    para almacenar el grafo.
    """

    def __init__(self):
        """
        Inicializa el grafo vacío.
        """
        self.grafo_dict = {}

    def agregar_vertice(self, vertice):
        """
        Agrega un vértice al grafo. Si el vértice ya existe, no hace nada.

        Args:
        vertice: El vértice a agregar al grafo
        """
        if vertice not in self.grafo_dict:
            self.grafo_dict[vertice] = []
        else:
            raise ValueError("El vértice ya existe en el grafo")

    def agregar_arista(self, edge):
        
        origen = edge.get_origen()
        destino = edge.get_destino()
        if origen not in self.grafo_dict:
            raise ValueError(f"Vertice {origen.get_name()} no existe en el grafo")
        if destino not in self.grafo_dict:
            raise ValueError(f"Vertice {destino.get_name()} no existe en el grafo")
        self.grafo_dict[origen].append(destino)

    def existe_vertice_en_grafo(self, vertice):
        """
        Verifica si un vértice existe en el grafo.

        Args:
        vertice: El vértice a verificar

        Returns:
        --------
        (bool): True si el vértice existe en el grafo, False en caso contrario.
        """
        return vertice in self.grafo_dict
    
    def get_vertex(self, vertex_name ):
        for vertex in self.grafo_dict:
            if vertex_name == vertex.get_name():
                return vertex
        print(f'El vertice {vertex_name} no existe en el grafo')

    #para los nodos vecinos o nodos hijos si vemos el grafo como un arbol
    def get_sons(self, vertex):
        return self.grafo_dict[vertex]
    
    def __str__(self):
        all_edges = ''
        for origen in self.grafo_dict:
            for destino in self.grafo_dict[origen]:
                all_edges += f'{origen.get_name()} --> {destino.get_name()}\n'