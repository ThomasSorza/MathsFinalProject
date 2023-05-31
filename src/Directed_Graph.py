import networkx as nx
import matplotlib.pyplot as plt
from Vertex import Vertex
from Edge import Edge


class Directed_Graph:
    """
    Representa un grafo dirigido con una lista de adyacencia.
    """

    def __init__(self):
        """
        Inicializa un nuevo objeto Directed_Graph con un diccionario vacío.
        """
        self.graph_dict = {}

    def add_vertex(self, vertex):
        """
        Añade un nuevo nodo al grafo.

        Parámetros:
            vertex (Vertex): El nodo que se agregará al grafo.
        """
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        Añade una nueva arista al grafo.

        Parámetros:
            edge (Edge): La arista que se agregará al grafo.
        """
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)

    def is_vertex_in(self, vertex):
        """
        Verifica si un nodo se encuentra en el grafo.

        Parámetros:
            vertex (Vertex): El nodo que se verificará.

        Retorna:
            True si el nodo se encuentra en el grafo, False en caso contrario.
        """
        return vertex in self.graph_dict

    def get_vertex(self, vertex_name):
        """
        Obtiene un nodo del grafo por nombre.

        Parámetros:
            vertex_name (str): El nombre del nodo que se va a buscar.

        Retorna:
            El nodo con el nombre especificado si se encuentra en el grafo, None en caso contrario.
        """
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')

    def get_neighbors(self, vertex):
        """
        Obtiene la lista de vecinos de un nodo.

        Parámetros:
            vertex (Vertex): El nodo del cual se va a buscar la lista de vecinos.

        Retorna:
            Una lista con la instancia de los vecinos del nodo.
        """
        return self.graph_dict[vertex]


    def BFS(self, start, end):
        """
        Ejecuta el algoritmo BFS (Breadth First Search) para encontrar la ruta más corta desde el nodo de inicio hasta el nodo de fin.

        Parámetros:
            start (Vertex): El nodo de inicio.
            end (Vertex): El nodo de fin.

        Retorna:
            Una lista con el recorrido desde el nodo de inicio hasta el nodo de fin.
        """
        path = [start]
        queue = [path]
        while queue:
            current_path = queue.pop(0)
            if current_path[-1] == end:
                return current_path
            for next_vertex in self.get_neighbors(current_path[-1]):
                if next_vertex not in current_path:
                    new_path = current_path + [next_vertex]
                    queue.append(new_path)

    def DFS_path(self, start, end, path, best):
        """
        Ejecuta el algoritmo DFS (Depth First Search) para encontrar la ruta más corta desde el nodo de inicio hasta el nodo de fin.

        Parámetros:
            start (Vertex): El nodo de inicio.
            end (Vertex): El nodo de fin.
            path (list): El camino actual en la recursión.
            best (list): El mejor camino encontrado hasta ahora.

        Retorna:
            Una lista con el recorrido desde el nodo de inicio hasta el nodo de fin.
        """
        path = path + [start]
        if start == end:
            return path
        for v in self.get_neighbors(start):
            if v not in path:
                if best is None or len(path) < len(best):
                    new_path = self.DFS_path(v, end, path, best)
                    if new_path is not None:
                        best = new_path
        return best

    def show_graph(self):
        """
        Muestra una representación gráfica del grafo utilizando la biblioteca NetworkX y Matplotlib.
        """
        G = nx.DiGraph()

        for vertex in self.graph_dict:
            G.add_node(vertex.get_name())

            for neighbor in self.get_neighbors(vertex):
                G.add_edge(vertex.get_name(), neighbor.get_name())

        pos = nx.spring_layout(G)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color='lightblue',
            edge_cmap=plt.cm.Blues,
            arrows=True,
            node_size=3000
        )
        plt.title("Representación de un cajero con un grafo dirigido")
        plt.show()

    def __str__(self):
        """
        Retorna una representación en forma de cadena de texto del grafo, mostrando todas las aristas.

        Retorna:
            str: La representación del grafo como una cadena de texto.
        """
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + '---->' + v2.get_name() + '\n'
        return all_edges
