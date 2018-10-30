from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.graph[(from_node, to_node)] = weight
        self.graph[(to_node, from_node)] = weight

graph = Graph()

edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
]

for edge in edges:
    graph.add_edge(*edge)

def kruskal_mst(graph):
    vistited_node = []
    sorted_graph = sorted(graph.graph.items(),key=lambda item: item[1])
    maxing_edges = (len(sorted_graph)/2)-1
    for edges, weight in sorted_graph:
        print(edges[0],edges[1])
        if len(vistited_node)>=maxing_edges:
            break

    print(vistited_node)

kruskal_mst(graph)