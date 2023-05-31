from Vertex import Vertex

class Edge:
    """
    Representa una arista en un grafo dirigido.
    """

    def __init__(self, v1, v2, cost=1):
        """
        Inicializa un nuevo objeto Edge.

        Parámetros:
            v1 (Vertex): El primer vértice de la arista.
            v2 (Vertex): El segundo vértice de la arista.
            cost (int): El costo o peso de la arista (predeterminado a 1).
        """
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

    def get_v1(self):
        """
        Obtiene el primer vértice de la arista.

        Retorna:
            Vertex: El primer vértice de la arista.
        """
        return self.v1

    def get_v2(self):
        """
        Obtiene el segundo vértice de la arista.

        Retorna:
            Vertex: El segundo vértice de la arista.
        """
        return self.v2
    
    def get_cost(self):
        """
        Obtiene el costo o peso de la arista.

        Retorna:
            int: El costo o peso de la arista.
        """
        return self.cost

    def __str__(self):
        """
        Retorna una representación en forma de cadena de texto de la arista.

        Retorna:
            str: La representación de la arista como una cadena de texto.
        """
        return f"{self.v1.get_name()} --({self.cost})--> {self.v2.get_name()}"
