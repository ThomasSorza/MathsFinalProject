import pyfiglet
from Directed_Graph import Directed_Graph
from Vertex import Vertex
from Edge import Edge
from test_values import build_graph
from Cola import Cola
import random

class View:
    def __init__(self):
        self.graph = Directed_Graph()
        self.G1 = build_graph(Directed_Graph)

    def display_graph(self):
        """
        Muestra la representación gráfica del grafo.
        """
        self.graph.show_graph()

    def preload_values(self):
        """
        Precarga valores y muestra opciones al usuario.
        """
        self.G1 = build_graph(Directed_Graph)
        secondOption = input(
            "Quieres ver el grafo de manera:\n1. Gráfica\n2. Por consola\n3. Mostrar transaccion con menos operaciones\n4. Mostrar x transaccion DFS\n"
        )
        if secondOption == "1":
            self.G1.show_graph()
        elif secondOption == "2":
            print(self.G1)
        elif secondOption == "3":
            print("Ruta mas corta usando algoritmo BFS: entre inicio y fin ")
            spath = self.G1.BFS(self.G1.get_vertex("inicio"), self.G1.get_vertex("fin"))
            print("\n")
            for v in spath:
                print(f"{v.get_name()} \n")
        elif secondOption == "4":
            print("Ruta mas corta usando algoritmo DFS: entre inicio y fin ")
            spath = self.G1.DFS_path(
                self.G1.get_vertex("inicio"), self.G1.get_vertex("fin"), [], None
            )
            print("\n")
            for v in spath:
                print(f"{v.get_name()} \n")
        else:
            print("Opción inválida")
            self.preload_values()

    def calculate_time(self):
        """
        Calcula el tiempo de espera en la cola y muestra el resultado.
        """
        try:
            total_suma = 0
            entero = int(input("Ingrese un entero (gente en Cola): "))
            cola = Cola(entero)
            suma_aleatoria = random.randint(48, 90)
            for i in range(entero):
                total_suma += suma_aleatoria

            print("La suma de tiempos es:", str(total_suma) + " segundos")
            print("El promedio de tiempo es:", str(total_suma / 60) + " minutos")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    def add_vertex_edge(self):
        """
        Agrega un nodo y una arista al grafo a partir de la entrada del usuario.
        """
        try:
            origin_name = input("Ingrese el nombre del nodo de origen de la arista: ")
            destination_name = input("Ingrese el nombre del nodo de destino de la arista: ")
            cost = float(input("Ingrese el costo (peso) de la arista: "))

            origin = self.graph.get_vertex(origin_name)
            if origin is None:
                origin = Vertex(origin_name)
                self.graph.add_vertex(origin)

            destination = self.graph.get_vertex(destination_name)
            if destination is None:
                destination = Vertex(destination_name)
                self.graph.add_vertex(destination)

            edge = Edge(origin, destination, cost)
            self.graph.add_edge(edge)
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar un número válido para el costo.")

class ViewMenu:
    def menuPrincipal(self):
        v = View()
        while True:
            word = pyfiglet.figlet_format("APP ATMs GRAFOS")
            print(word)
            print(
                "*** Grafos Solucion Cajeros automaticos: Menú Principal *** \n\n1. Iniciar con valores precargados\n2. Ingresar valores (operaciones)\n3. Mostrar Grafo\n4. Calcular Tiempo en la fila\n\n0. Salir\n"
            )
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print("Ha seleccionado la Opción 1")
                v.preload_values()
            elif opcion == "2":
                print("Ha seleccionado la Opción 2")
                v.add_vertex_edge()
            elif opcion == "3":
                print("Ha seleccionado la Opción 3")
                v.display_graph()
            elif opcion == "4":
                print("Ha seleccionado la Opción 4")
                v.calculate_time()
            elif opcion == "0":
                print("Finalizando el programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    print("HolaMundo")
    view_menu = ViewMenu()
    view_menu.menuPrincipal()
