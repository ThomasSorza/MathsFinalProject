from Vertex import Vertex

class Edge:
    def __init__(self, v1, v2, cost=1):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2
    
    def get_cost(self):
        return self.cost

    def __str__(self):
        return f"{self.v1.get_name()} --({self.cost})--> {self.v2.get_name()}"
