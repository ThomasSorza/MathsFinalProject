from Vertex import Vertex

class Edge:
    def __init__(self, origin, destination, cost):
        self.origin = origin
        self.destination = destination
        self.cost = cost

    def get_origin(self):
        return self.origin
    
    def get_destination(self):
        return self.destination
    
    def get_cost(self):
        return self.cost
    
    def __str__(self):
        return f'{self.origin.get_name()} --> {self.destination.get_name()} ({str(self.cost)})'
