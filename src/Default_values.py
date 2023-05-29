from Directed_Graph import Directed_Graph
from Undirected_Graph import Undirected_Graph
from Edge import Edge
from Vertex import Vertex

def build_graph(graph_class):
    g = graph_class()
    for v in ('Insertar_tarjeta','Ingreso', 'Transferencia', 'Numero_cuenta', 'Retirar', 'Tipo_cuenta', 'Ingrese_pin', 'Consulta_saldo', 'Fin', 'Ingreso_cuenta', 'Cambio_pin'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('Ingreso'), g.get_vertex('Insertar_tarjeta'), 1))
    g.add_edge(Edge(g.get_vertex('Ingreso'), g.get_vertex('Transferencia'), 6))
    g.add_edge(Edge(g.get_vertex('Ingreso'), g.get_vertex('Retirar'), 1))
    g.add_edge(Edge(g.get_vertex('Insertar_tarjeta'), g.get_vertex('Transferencia'), 1))
    g.add_edge(Edge(g.get_vertex('Insertar_tarjeta'), g.get_vertex('Retirar'), 1))
    g.add_edge(Edge(g.get_vertex('Insertar_tarjeta'), g.get_vertex('Consulta_saldo'), 1))
    g.add_edge(Edge(g.get_vertex('Insertar_tarjeta'), g.get_vertex('Ingreso_cuenta'), 1))
    g.add_edge(Edge(g.get_vertex('Transferencia'), g.get_vertex('Tipo_cuenta'), 1))
    g.add_edge(Edge(g.get_vertex('Retirar'), g.get_vertex('Numero_cuenta'), 1))
    g.add_edge(Edge(g.get_vertex('Retirar'), g.get_vertex('Tipo_cuenta'), 1))
    g.add_edge(Edge(g.get_vertex('Tipo_cuenta'), g.get_vertex('Numero_cuenta'), 1))
    g.add_edge(Edge(g.get_vertex('Numero_cuenta'), g.get_vertex('Ingrese_pin'), 1))
    g.add_edge(Edge(g.get_vertex('Ingreso_cuenta'), g.get_vertex('Cambio_pin'), 1))
    g.add_edge(Edge(g.get_vertex('Cambio_pin'), g.get_vertex('Ingrese_pin'), 1))
    g.add_edge(Edge(g.get_vertex('Ingrese_pin'), g.get_vertex('Consulta_saldo'), 1))
    g.add_edge(Edge(g.get_vertex('Ingrese_pin'), g.get_vertex('Fin'), 1))
    g.add_edge(Edge(g.get_vertex('Consulta_saldo'), g.get_vertex('Fin'), 1))
    return g

G1 = build_graph(Directed_Graph)
print(G1)
G1.show_graph()