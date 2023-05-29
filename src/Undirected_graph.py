from Directed_Graph import Directed_Graph
from Edge import Edge

class Undirected_Graph(Directed_Graph):

    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_inverted = Edge(edge.get_destination(), edge.get_origin(), edge.get_cost())
        Directed_Graph.add_edge(self, edge_inverted)