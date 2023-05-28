from Vertex import Vertex
from Edge import Edge

class Directed_Graph:

    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
        else:
            raise ValueError("El vértice ya existe en el grafo")

    def add_edge(self, edge):
        origin = edge.get_origin()
        destination = edge.get_destination()
        if origin not in self.graph_dict:
            raise ValueError(f"Vertice {origin.get_name()} no existe en el grafo.")
        if destination not in self.graph_dict:
            raise ValueError(f"Vertice {destination.get_name()} no existe en el grafo.")
        self.graph_dict[origin].append(destination)

    def is_vertex_in_graph(self, vertex):
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name ):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'El vertice {vertex_name} no existe en el grafo.')

    #para los nodos vecinos o nodos hijos si vemos el grafo como un arbol
    def get_sons(self, vertex):
        return self.graph_dict[vertex]
    
    def __str__(self):
        all_edges = ''
        for origin in self.graph_dict:
            for destination in self.graph_dict[origin]:
                all_edges += f'{origin.get_name()} --> {destination.get_name()}\n'
        return all_edges