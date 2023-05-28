from Directed_Graph import Directed_Graph
from Edge import Edge
from Vertex import Vertex

def build_graph(graph_class):
    g = graph_class()
    for v in ('Ingreso', 'Transferencia', 'Numero_cuenta', 'Retirar', 'Tipo_cuenta', 'Ingrese_pin', 'Consulta_saldo', 'Fin', 'Ingreso_cuenta', 'Cambio_pin'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('Ingreso'), g.get_vertex('Transferencia'), 1))
    return g

G1 = build_graph(Directed_Graph)
print(G1)
