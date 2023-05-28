
class Vertex:
    """
    Clase que representa un vértice en un grafo.

    Attributes:
    ----------
    name : str
        Nombre del vértice.
    """

    def __init__(self, name):
        """
        Inicializa el vértice con un nombre.

        Args:
        name : str
            Nombre del vértice.
        """
        self.name = name

    def get_name(self):
        """
        Devuelve el nombre del vértice.

        Returns:
        --------
        (str): Nombre del vértice.
        """
        return self.name
    
    def __str__(self):
        """
        Devuelve una representación en string del vértice.

        Returns:
        --------
        (str): Representación en string del vértice.
        """
        return self.name
