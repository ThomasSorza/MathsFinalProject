from Directed_Graph import Directed_Graph
from Default_values import Default_values

class View:
    def __init__(self):
        self.graph = Directed_Graph()

    def display_graph(self):
        self.graph.show_graph()

   # def 

class ViewMenu:

    def menuPrincipal():
        while True:
            print("*** Bienvenido a nuestro Menú Principal *** \n1. Iniciar con valores preterminados\n2. Ingresar valores\n3. Mostrar Grafo\n\n0. Salir\n")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print("Hola1")
                menuTarjeta()
            elif opcion == "2":
                print("Ha seleccionado la Opción 2")
                # Aquí puedes colocar el código correspondiente a la opción 2
        
            elif opcion == "3":
                print("Ha seleccionado la Opción 3")
                # Crear una instancia de la clase View
                v = View()
                v.display_graph()
            
                print("No sucede nada")
    
            elif opcion == "0":
                print("Todo bien")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
    
    if __name__ == "__main__":
        print("HolaMundo")
        menuPrincipal()





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



  
    