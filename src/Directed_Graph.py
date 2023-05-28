import networkx as nx
import matplotlib.pyplot as plt
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
        self.graph_dict[origin].append(edge)
        self.graph_dict[destination].append(edge)

    def is_vertex_in_graph(self, vertex):
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'El vertice {vertex_name} no existe en el grafo.')
    
    def get_neighbors(self, vertex):
        return self.graph_dict[vertex]
    
    def show_graph(self):
        G = nx.Graph()
        for vertex in self.graph_dict:
            G.add_node(vertex.get_name())
        for vertex, edges in self.graph_dict.items():
            for edge in edges:
                destination = edge.get_destination()
                cost = edge.get_cost()
                G.add_edge(vertex.get_name(), destination.get_name(), weight=cost)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
    
    def __str__(self):
        all_edges = ''
        for origin in self.graph_dict:
            for edge in self.graph_dict[origin]:
                destination = edge.get_destination()
                cost = edge.get_cost()
                all_edges += f'{origin.get_name()} --({cost})-- {destination.get_name()}\n'
        return all_edges
