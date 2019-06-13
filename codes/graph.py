# @Param nodes é um conjunto de Vértices
# @Param edges é um conjunto de arestas, ou seja, tuplas de Vértices

from copy import deepcopy

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.nodes_edges = {}
    

    # @Param node é um vértice
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.nodes_edges[node] = []

    # @Param node é um vértice
    def rem_node(self, node):
        self.nodes.remove(node)
        self.nodes_edges.pop(node)
        for no, ed in self.nodes_edges.items():
            for tup in ed:
                if(no == tup[0] or no == tup[1]):
                    self.nodes_edges[no].remove(tup);

    # @Param nodes é um vetor de vértices
    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    # @Param nodes é um vetor de nodes
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

    # @Param edge é uma tupla de vértices
    def rem_edge(self, edge):
        self.edges.remove(edge);
        self.nodes_edges[edge[0]].remove(edge)
        self.nodes_edges[edge[1]].remove(edge)

    # @Param edges é um vetor de tuplas de vértices
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    # @Param edges é um vetor de tuplas de vértices
    def rem_edges(self, edges):
        for edge in edges:
            self.rem_edge(edge)

    # @Return Número de nós
    def number_of_nodes(self):
        return len(self.nodes)

    # @Return Se dois grafos tem o mésmo numero de nós
    def same_number_of_nodes(self, G):
        if(self.number_of_nodes() == G.number_of_nodes()):
            return True
        return False

    # @Return número de arestas
    def number_of_edges(self):
        return len(self.edges);

    # @Return True se dois grafos tem mesma quantidade de arestas
    def same_number_of_edges(self, G):
        if(self.number_of_edges() == G.number_of_edges()):
            return True
        return False

    # @Return sequência de graus
    def degree_sequence(self):
        lista = sorted([len(node) for node in self.nodes_edges.values()],reverse=True)
        return lista

    # @Return True se dois grafos tem mesma sequencia de graus
    def same_degree_sequence(self, G):
        if not(self.same_number_of_nodes(G)):
            return False
            
        self_degree_seq = self.degree_sequence()
        G_degree_seq = G.degree_sequence()

        for i in range(self.number_of_nodes()):
            if(self_degree_seq[i] != G_degree_seq[i]):
                return False

        return True

    # @Return 
    def node_with_a_degree(self, degree):
        for node in self.nodes_edges.items():
            if(len(node[1]) == degree):
                self.rem_node(node[0])
                return node[0]

        return False



    # @Return o nó de maior grau
    def highest_degree_node(self):
        highest_degree = 0;
        highest_node = None;
        for node in self.nodes:
            if(highest_degree < len(self.nodes_edges[node])):
                highest_degree = len(self.nodes_edges[node])
                highest_node = node

        return highest_node;

    # @Return o nó de maior grau
    def highest_degree_node_from_list(self, lista):
        highest_degree = 0;
        highest_node;
        for node in nodes:
            if node in lista:
                if(highest_degree < len(nodes_edges[node])):
                    highest_degree = len(nodes_edges[node])
                    highest_node = node

        return highest_node;

    # @Return Lista de adjacencia
    def adjacency_list(self):
        adjacency = {node: {'neighbors':self.neighbors_nodes(self, node), 'number_of_descendants':0} for node in self.nodes_edges.keys()}

    # @Return dicionário com chaves sendo nós e valores sendo a quantidade de descendentes de cada nó
    '''    def number_of_descendants(self):
        visited = []
        non_visited = self.nodes.copy()
        self_adjacency = self.adjacency_list() # Dicionario
        # Para cada nó calcular 

        for n in self_adjacency:
            if(self_adjacency[n]['number_of_descendants'] != 0):
                descendants_of_n = 0
                for neighbor in self_adjacency[n]['neighbors']:
                    if(neighbor not in visited):
                        non_visited.remove(neighbor);
                        visited.append(neighbor);
                        # calcular número de descendentes de neighbor
    '''


    def nodes_same_degree(self, degree):
        return [key for key,item in self.nodes_edges.items() if len(item) == degree]

    def init_highest_degree(self, H):
        degree = self.degree_sequence()[0]
        G_degrees = self.nodes_same_degree(degree)
        H_degrees = H.nodes_same_degree(degree)
        return G_degrees, H_degrees


    # @Return vértices adjacentes
    def neighbors_nodes(self, node):
        list_neighbors = []
        for neighbor in self.nodes_edges[node]:
            if(neighbor[0] == node): list_neighbors.append(neighbor[1])
            elif(neighbor[1] == node): list_neighbors.append(neighbor[0])
        return list_neighbors

    # @Return True se dois grafos são isomorfos
    def is_isomorphic(self, H):
        if not(self.same_number_of_nodes(H)):
            return False
        if not(self.same_number_of_edges(H)):
            return False
        if not(self.same_degree_sequence(H)):
            return False

        # Dicionário contendo o vértice e seu grau
        dict1 = {}
        for key, item in self.nodes_edges.items():
            dict1[key] = len(item)

        print("Dicionário com graus dos nós do grafo 1")
        print(dict1)

        
        dict2 = {}
        for key, item in H.nodes_edges.items():
            dict2[key] = len(item)
        
        print("Dicionário com graus dos nós do grafo 2")
        print(dict2)

        #Dicionário contendo o mapeamento dos nós/resposta final
        result = {}

        # Mapeando nós
        for node1 in dict1.items():
            for node2 in dict2.items():
                if node1[1] == node2[1] and node2[0] not in result.values():
                    result[node1[0]] = node2[0]


        print("\n## Grafos possuem mesma sequência de graus ##\n")
        print("PODE SER FEITA UMA BIJEÇÃO ENTRE OS NÓS DOS GRAFOS ")
        
        print('\nPossível Resultado:')
        print(result)

        return result
        
        


        #eturn True