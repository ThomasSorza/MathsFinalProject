import Graph
import Edge

class Undirected_graph(Graph):

    def add_edge(self, edge):
        """
        Adds a new edge to the graph.
        """
        Graph.agregar_arista(self, edge)
        edge_inverted = Edge(edge.get_destino(), edge.get_origen(), edge.get_peso())
        Graph.agregar_arista(self, edge_inverted)