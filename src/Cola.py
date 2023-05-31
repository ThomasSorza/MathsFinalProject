class Cola:
    """
    Representa una cola con una longitud máxima y operaciones básicas de inserción, eliminación y visualización.
    """

    def __init__(self, longitud):
        """
        Inicializa un nuevo objeto Cola.

        Parámetros:
            longitud (int): La longitud máxima de la cola.
        """
        self.lista_personas = []
        self.longitud = longitud

    def get_lista_personas(self):
        """
        Obtiene la lista de personas en la cola.

        Retorna:
            list: La lista de personas en la cola.
        """
        return self.lista_personas

    def push(self, elemento):
        """
        Agrega un elemento a la cola.

        Parámetros:
            elemento: El elemento que se agregará a la cola.
        """
        if len(self.lista_personas) < self.longitud:
            self.lista_personas.append(elemento)
        else:
            print("La cola está llena")

    def pop(self):
        """
        Elimina y devuelve el primer elemento de la cola.

        Retorna:
            El primer elemento de la cola.
        """
        if len(self.lista_personas) > 0:
            return self.lista_personas.pop(0)
        else:
            print("La cola está vacía")

    def imprimir_cola(self):
        """
        Imprime los elementos en la cola.
        """
        print("Elementos en la cola:", self.lista_personas)

    def sumatoria_tiempos(self):
        """
        Calcula la sumatoria de los tiempos en la cola.

        Retorna:
            La sumatoria de los tiempos en la cola.
        """
        total_time = 0
        for tiempo in self.lista_personas:
            total_time += tiempo
        return total_time
    
    def __str__(self):
        """
        Retorna una representación en forma de cadena de texto de la cola.

        Retorna:
            str: La representación de la cola como una cadena de texto.
        """
        return f'Cola con {len(self.lista_personas)} personas en espera'
