import Graph
import Edge
import Vertex

def build_graph(Graph):
    g = Graph()
    for v in ('Ingreso', 'Transferencia', 'Numero_cuenta', 'Retirar', 'Tipo_cuenta', 'Ingrese_pin', 'Consulta_saldo', 'Fin', 'Ingreso_cuenta', 'Cambio_pin'):
        g.agregar_vertice(Vertex(v))
    g.agregar_arista(Edge(g.get_vertex('Ingreso'), g.get_vertex('Transferencia'), 1))

    return g

G1 = build_graph(Graph)