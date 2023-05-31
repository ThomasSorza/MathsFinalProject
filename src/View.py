from Directed_Graph import Directed_Graph
from Vertex import Vertex
from Edge import Edge
from test_values import build_graph
from Cola import Cola

class View:
    
    def __init__(self):
        self.graph = Directed_Graph()

    def display_graph(self):
        self.graph.show_graph()

    #primera opcion
    def preload_values(self):
        G1 = build_graph(Directed_Graph)
        secondOption = input("Quieres ver el grafo de manera:\n1. Gráfica\n2. Por consola\n")
        if secondOption == "1":
            G1.show_graph()
        elif secondOption == "2":
            print(G1)

    #segunda opcion
    def add_vertex_edge(self):
        # Solicitar información al usuario para crear el nodo
        origin_name = input("Ingrese el nombre del nodo de origen de la arista: ")
        destination_name = input("Ingrese el nombre del nodo de destino de la arista: ")
        cost = float(input("Ingrese el costo(peso) de la arista: "))

        # Buscar o crear los nodos correspondientes
        origin = self.graph.get_vertex(origin_name)
        if origin is None:
            origin = Vertex(origin_name)
            self.graph.add_vertex(origin)

        destination = self.graph.get_vertex(destination_name)
        if destination is None:
            destination = Vertex(destination_name)
            self.graph.add_vertex(destination)

        # Crear la arista
        edge = Edge(origin, destination, cost)

        # Agregar la arista al grafo
        self.graph.add_edge(edge)

import pyfiglet

class ViewMenu:
    def menuPrincipal(self):
        v = View()  # Crear una instancia de la clase View
        while True:
            word=pyfiglet.figlet_format('APP ATMs GRAFOS')
            print(word)
            print("*** Grafos Solucion Cajeros automaticos: Menú Principal *** \n\n1. Iniciar con valores precargados\n2. Ingresar valores (operaciones)\n3. Mostrar Grafo\n4. Mostrar transaccion con menos operaciones\n5. Calcular Tiempo en la fila\n\n0. Salir\n")
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
                print("No sucede nada")
            elif opcion == "4":
                print("Ha seleccionado la Opción 4")
            elif opcion == "5":
                print("Ha seleccionado la Opción 5")
            elif opcion == "0":
                print("Finalizando el programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    print("HolaMundo")
    view_menu = ViewMenu()
    view_menu.menuPrincipal() 