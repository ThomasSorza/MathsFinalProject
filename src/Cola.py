class Cola:
    def __init__(self, longitud):
        self.lista_personas = []
        self.longitud = longitud

    def push(self, elemento):
        if len(self.lista_personas) < self.longitud:
            self.lista_personas.append(elemento)
        else:
            print("La cola está llena")

    def pop(self):
        if len(self.lista_personas) > 0:
            return self.lista_personas.pop(0)
        else:
            print("La cola está vacía")

    def imprimir_cola(self):
        print("Elementos en la cola:", self.lista_personas)

    def sumatoria_tiempos(self):
        total_time = 0
        for tiempo in self.lista_personas:
            total_time += tiempo
        return total_time
    
    def __str__(self):
        return f'Cola con {len(self.lista_personas)} personas en espera'


