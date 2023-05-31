from Undirected_graph import Undirected_Graph
from Directed_Graph import Directed_Graph
from Vertex import Vertex
from Edge import Edge

class View:
    def __init__(self):
        self.graph = Directed_Graph()

    def display_graph(self):
        self.graph.show_graph()

    def add_vertex_edge(self):
        # Solicitar información al usuario
        name = input("Ingrese el nombre del nodo: ")
        origin_name = input("Ingrese el nombre del nodo de origen de la arista: ")
        destination_name = input("Ingrese el nombre del nodo de destino de la arista: ")
        cost = float(input("Ingrese el costo de la arista: "))

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

class ViewMenu:
    def menuPrincipal(self):
        v = View()  # Crear una instancia de la clase View
        while True:
            print("*** Bienvenido a nuestro Menú Principal *** \n1. Iniciar con valores preterminados\n2. Ingresar valores\n3. Mostrar Grafo\n\n0. Salir\n")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print("Hola1")
                #menuTarjeta()
            elif opcion == "2":
                print("Ha seleccionado la Opción 2")
                v.add_vertex_edge()
            elif opcion == "3":
                print("Ha seleccionado la Opción 3")
                v.display_graph()
                print("No sucede nada")
            elif opcion == "0":
                print("Todo bien")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    print("HolaMundo")
    view_menu = ViewMenu()
    view_menu.menuPrincipal()
