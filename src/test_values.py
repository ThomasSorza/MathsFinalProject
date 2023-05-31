from Directed_Graph import Directed_Graph
from Undirected_Graph import Undirected_Graph
from Edge import Edge
from Vertex import Vertex

def build_graph(graph):
    """
    Builds a graph based on the provided graph class.

    Args:
    graph: The class of the graph to build.

    Returns:
    The generated graph instance.
    """
    g = graph()
    for v in ('inicio','transferencia', 'retirar', 'insertar_tarjeta', 'consulta_saldo', 'ingreso_cuenta', 'tipo_cuenta', 'numero_cuenta', 'cambio_pin', 'ingrese_pin', 'fin'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('inicio'), g.get_vertex('transferencia'),30))
    g.add_edge(Edge(g.get_vertex('inicio'), g.get_vertex('retirar'),30))
    g.add_edge(Edge(g.get_vertex('inicio'), g.get_vertex('insertar_tarjeta'),20))
    g.add_edge(Edge(g.get_vertex('insertar_tarjeta'), g.get_vertex('transferencia'),35))
    g.add_edge(Edge(g.get_vertex('insertar_tarjeta'), g.get_vertex('retirar'),25))
    g.add_edge(Edge(g.get_vertex('insertar_tarjeta'), g.get_vertex('consulta_saldo'),20))
    g.add_edge(Edge(g.get_vertex('insertar_tarjeta'), g.get_vertex('ingreso_cuenta'),35))
    g.add_edge(Edge(g.get_vertex('transferencia'), g.get_vertex('tipo_cuenta'),10))
    g.add_edge(Edge(g.get_vertex('retirar'), g.get_vertex('tipo_cuenta'),50))
    g.add_edge(Edge(g.get_vertex('retirar'), g.get_vertex('numero_cuenta'),70))
    g.add_edge(Edge(g.get_vertex('tipo_cuenta'), g.get_vertex('numero_cuenta'),40))
    g.add_edge(Edge(g.get_vertex('numero_cuenta'), g.get_vertex('ingrese_pin'),1))
    g.add_edge(Edge(g.get_vertex('ingreso_cuenta'), g.get_vertex('cambio_pin'),35))
    g.add_edge(Edge(g.get_vertex('cambio_pin'), g.get_vertex('ingrese_pin'),23))
    g.add_edge(Edge(g.get_vertex('consulta_saldo'), g.get_vertex('ingrese_pin'),22))
    g.add_edge(Edge(g.get_vertex('ingrese_pin'), g.get_vertex('consulta_saldo'),22))
    g.add_edge(Edge(g.get_vertex('ingrese_pin'), g.get_vertex('ingrese_pin'),30))
    g.add_edge(Edge(g.get_vertex('ingrese_pin'), g.get_vertex('fin'),29))

    return g
