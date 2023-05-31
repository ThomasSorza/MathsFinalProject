from Directed_Graph import Directed_Graph
from Default_values import Default_values
from Edge import Edge

class View:
    def __init__(self):
        self.graph = Directed_Graph()

    def display_graph(self):
        self.graph.show_graph()

   # def 

class ViewMenu:
    def menuPrincipal(self):
        while True:
            print("*** Bienvenido a nuestro Menú Principal ***")
            print("1. Iniciar con valores preterminados")
            print("2. Ingresar valores")
            print("3. Mostrar Grafo")
            print("4. Mostrar transacciones con menos tiempo")
            print("5. Calcular tiempo en la fila")
            print("0. Salir")
            
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.menuShowGrafo()

            elif opcion == "2":
                self.menuObtainData()
        
            elif opcion == "3":
                self.menuGrafo

            elif opcion == "4":
                self.menuLestTime

            elif opcion == "5":
                self.tiempoEnFila

            elif opcion == "0":
                print("Todo bien")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    def menuShowGrafo(self):
        secondOption = input("Quieres ver el grafo de manera:\n1. Gráfica\n2. Por consola")
        if secondOption == "1":
            Directed_Graph.show_graph()

        elif secondOption == "2":
            print(Default_values.G1)

    def menuObtainData():
        print("Ingrese las operaciones propias")
        input("Ingrese el Nombre del nodo")
        print("\n\nIngrese la arista:")
        Edge(input("Nombre del nodo inicio"), input("Nombre del nodo salida"))
        print("El peso es ")

    def menuGrafo():
        print("A continuación se mostrará el grafo")
        v = View()
        v.display_graph()

    def menuLestTime():
        print("Las operaciones con menor tiempo fueron: " + "con BFS" + " y " + " con DFS")

    def tiempoEnFila():
        option = input("Seleccione una de las opciones")
        if option == "1":
            input("Ingrese la cantidad de personas en la fila.")
        elif option =="2":
            input("Calcular el tiempo de la cola")

if __name__ == "__main__":
    print("Hola Mundo")
    menu = ViewMenu()
    menu.menuPrincipal()

    """def menuTransferencia():
        #print("Por favor ingrese el numero de cuenta")
        opcion = input("Ingrese el tipo de cuenta:\n1. Ahorros\n2. corriente\n0. Salir")
        opcionNumeroCuenta = ""
        if opcion == "1":
            opcionNumeroCuenta =  input("Por favor ingrese el numero de cuenta:\n")
        #if opcionNumeroCuenta !=0:

        #elif opcion == "2":
            #print("")"""


    """def menuTarjeta():
        optionTarjeta = ""
        while True:
            print("** Menú Tarjeta**\n1. Trasferencia\n2. Retirar\n3. Ingreso Cuenta\n4. Consultar saldo\n0. Salir\n")
            optionTarjeta = input("Ingrese una opción: ")
            if optionTarjeta == "1":
                menuTransferencia()
            elif optionTarjeta == "2":
                print("La buena")
            break"""



  
    