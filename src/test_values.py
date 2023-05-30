from Directed_Graph import Directed_Graph
from Undirected_Graph import Undirected_Graph
from Edge import Edge
from Vertex import Vertex

def build_graph(graph):
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
    g.add_edge(Edge(g.get_vertex('cambio_pin'), g.get_vertex('ingrese_pin'),1))
    g.add_edge(Edge(g.get_vertex('consulta_saldo'), g.get_vertex('ingrese_pin'),1))
    g.add_edge(Edge(g.get_vertex('ingrese_pin'), g.get_vertex('consulta_saldo'),1))
    g.add_edge(Edge(g.get_vertex('ingrese_pin'), g.get_vertex('ingrese_pin'),1))
    g.add_edge(Edge(g.get_vertex('ingrese_pin'), g.get_vertex('fin'),1))
    
    return g

G1 = build_graph(Directed_Graph)
print(G1)

print('BFS:')
spath = G1.BFS(G1.get_vertex('inicio'), G1.get_vertex('fin'))
for v in spath:
    print(f'{v.get_name()} ', end='-> ')

print('\nDFS:')
path_1 = G1.DFS_path( G1.get_vertex('inicio'), G1.get_vertex('fin'), [], None)
for v in path_1:
    print(f'"{v.get_name()}"', end=' ')

G1.show_graph()
