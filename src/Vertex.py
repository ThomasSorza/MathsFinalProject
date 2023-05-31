class Vertex:
    """
    This class represents a Vertex in a graph.

    Args:
    name: The name of the vertex.

    Attributes:
    name: The name of the vertex.

    Methods:
    get_name: Returns the name of the vertex.
    __str__: Returns the string representation of the vertex, which is its name.
    """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Returns the name of the vertex.

        Args:
        None

        Returns:
        The name of the vertex.
        """
        return self.name
    
    def __str__(self):
        """
        Returns the string representation of the vertex, which is its name.

        Args:
        None

        Returns:
        The name of the vertex.
        """
        return self.get_name()
