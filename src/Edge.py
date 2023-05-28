class Edge:

    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def get_origen(self):
        return self.origen
    
    def get_destino(self):
        return self.destino
    
    def __str__(self):
        return self.origen.get_name() + " --> " + self.destino.get_name() + " (" + str(self.peso) + ")"