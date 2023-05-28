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

    def agregar_arista(self, origen, destino, peso):
        """
        Agrega una arista al grafo.

        Args:
        origen: El vértice de origen de la arista.
        destino: El vértice de destino de la arista.
        peso: Peso de la arista.
        """
        self.aristas.append((origen, destino, peso))
