from Directed_Graph import Directed_Graph
from Edge import Edge

class Undirected_Graph(Directed_Graph):
    """
    Una subclase de Directed_Graph que también agrega aristas invertidas para
    crear un grafo no dirigido.
    """

    def add_edge(self, edge):
        """
        Agrega una arista al grafo y su arista invertida correspondiente.

        Parámetros:
            edge (Edge): la arista a agregar.
        """
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        Directed_Graph.add_edge(self, edge_back)
