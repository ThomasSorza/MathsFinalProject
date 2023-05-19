# Definición de la clase Grafo
class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []

    def agregar_nodo(self, nodo):
        self.nodos[nodo] = []

    def agregar_arista(self, origen, destino):
        self.aristas.append((origen, destino))
        self.nodos[origen].append(destino)
        self.nodos[destino].append(origen)

    def buscar_ruta(self, origen, destino):
        visitados = set()
        pila = [(origen, [])]

        while pila:
            actual, ruta = pila.pop()

            if actual == destino:
                return ruta + [actual]

            if actual not in visitados:
                visitados.add(actual)

                for vecino in self.nodos[actual]:
                    if vecino not in visitados:
                        pila.append((vecino, ruta + [actual]))

        return None


# Crear una instancia del grafo
grafo = Grafo()

# Agregar nodos para representar los cajeros automáticos
grafo.agregar_nodo('Cajero1')
grafo.agregar_nodo('Cajero2')
grafo.agregar_nodo('Cajero3')
grafo.agregar_nodo('Cajero4')

# Agregar aristas para representar las conexiones entre los cajeros automáticos
grafo.agregar_arista('Cajero1', 'Cajero2')
grafo.agregar_arista('Cajero1', 'Cajero3')
grafo.agregar_arista('Cajero2', 'Cajero4')
grafo.agregar_arista('Cajero3', 'Cajero4')

# Realizar una búsqueda de ruta para encontrar un camino entre dos cajeros automáticos
ruta = grafo.buscar_ruta('Cajero1', 'Cajero4')

# Verificar el resultado
if ruta:
    print("Ruta encontrada:", ruta)
else:
    print("No se encontró ninguna ruta.")
