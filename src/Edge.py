import Vertex

class Edge:
    """Class for defining an Edge in a Graph"""

    def __init__(self, origen, destino, peso):
        """
        Initializes the attributes of an Edge object.

        Arguments:
        origen - vertex where the edge begins
        destino - vertex where the edge ends
        peso - numerical weight of the edge
        """
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def get_origen(self):
        """
        Returns the Vertex object where the edge begins
        """
        return self.origen
    
    def get_destino(self):
        """
        Returns the Vertex object where the edge ends
        """
        return self.destino
    
    def __str__(self):
        """
        Returns a string representing the Edge object in the format:
        "source --> destination (weight)"
        """
        return self.origen.get_name() + " --> " + self.destino.get_name() + " (" + str(self.peso) + ")"
