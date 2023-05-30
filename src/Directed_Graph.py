import networkx as nx
import matplotlib.pyplot as plt
from Vertex import Vertex
from Edge import Edge


class Directed_Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = []

    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)

    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict

    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')

    def get_neighbors(self, vertex):
        return self.graph_dict[vertex]


    #algoritmo de Busqueda Breadth First Search
    def BFS(self, start, end):
        '''
        graph - Graph object
        start - Origen vertex/node
        end - Destination vertex/node
        '''
        path = [start]
        queue = [path]
        #run all the queue
        while queue:
            current_path = queue.pop(0)
            if current_path[-1] == end:
                return current_path
            for next_vertex in self.get_neighbors(current_path[-1]):
                if next_vertex not in current_path:
                    new_path = current_path + [next_vertex]
                    queue.append(new_path)

    #algoritmo de Busqueda Depth First Search
    def DFS_path(self, start, end, path, best):
        path = path + [start]
        # base case
        if start == end:
            return path
        for v in self.get_neighbors(start):
            if v not in path:
                if best == None or len(path) < len(best):
                    new_path = self.DFS_path( v,  end, path, best)
                    if new_path is not None:
                        best = new_path
        return best

    def show_graph(self):
        G = nx.DiGraph()

        for vertex in self.graph_dict:
            G.add_node(vertex.get_name())

            for neighbor in self.get_neighbors(vertex):
                G.add_edge(vertex.get_name(), neighbor.get_name())

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_cmap=plt.cm.Blues, arrows=True)
        plt.show()


    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + '---->' + v2.get_name() + '\n'
        return all_edges


