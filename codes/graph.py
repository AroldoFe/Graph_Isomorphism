# @Param nodes é um conjunto de Vértices
# @Param edges é um conjunto de arestas, ou seja, tuplas de Vértices

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.nodes_edges = {}
  
    def __inint__(self, nodes, edges):
        self.add_nodes(nodes)
        self.add_edges(edges)
  
    # @Param node é um vértice
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.nodes_edges[node] = []
  
    def rem_node(self, node):
        self.nodes.remove(node)
        self.nodes_edges.pop(node)

    # @Param nodes é um vetor de vértices
    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def rem_nodes(self, nodes):
        for node in nodes:
            self.rem_node(node)
  
    # @Param edge é uma tupla de vértices
    def add_edge(self, edge):
        self.add_nodes(list(edge))
    
        if( ((edge[0], edge[1]) not in self.edges) and
            ((edge[1], edge[0]) not in self.edges) ):
            self.edges.append(edge);
            self.nodes_edges[edge[0]].append(edge)
            self.nodes_edges[edge[1]].append(edge)
  
    def rem_edge(self, edge):
        self.edges.remove(edge);
        self.nodes_edges[edge[0]].remove(edge)
        self.nodes_edges[edge[1]].remove(edge)

    # @Param edges é um vetor de tuplas de vértices
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def rem_edges(self, edges):
        for edge in edges:
            self.rem_edge(edge)

    #
    def