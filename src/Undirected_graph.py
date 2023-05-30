from Directed_Graph import Directed_Graph
from Edge import Edge

class Undirected_Graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        Directed_Graph.add_edge(self, edge_back)
