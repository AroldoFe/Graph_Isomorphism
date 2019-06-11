# @Param nodes é um conjunto de Vértices
# @Param edges é um conjunto de arestas, ou seja, tuplas de Vértices

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.nodes_edges = {}
    
    '''
    def __inint__(self, nodes, edges):
        self.add_nodes(nodes)
        self.add_edges(edges)
    '''

    # @Param node é um vértice
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.nodes_edges[node] = []

    # @Param node é um vértice
    def rem_node(self, node):
        self.nodes.remove(node)
        self.nodes_edges.pop(node)

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


    def node_with_a_degree(self, degree):
        for node in self.nodes_edges.items():
            if(len(node[1]) == degree):
                self.rem_node(node[0])
                return node[0]

        return False

    # @Return True se dois grafos são isomorfos
    def is_isomorphic(self, G):
        if not(self.same_number_of_nodes(G)):
            return False
        if not(self.same_number_of_edges(G)):
            return False
        if not(self.same_degree_sequence(G)):
            return False

        '''
            Estratégia de Isomorfismo de grafos
            * Pode fazer um dicionario de vértice com seus vértices adjacentes
            * Tentar projetar um vértice no de mesmo grau e fazer com seus adjacentes

            * Tentar ligar dois grafos por arestas de modo que todo vértice de um grafo G deve estar ligado a exatamente um vértice de H
            * Se existe algum nó de G que não está ligado a H, então não são isomorfos
            * dois vértices x,y serão "isomorfos" se existe ciclo de tamanho 4 passando por 2 arestas de ligação de grafos para todas as arestas de x (exemplo de cubo que o plano da frente é isomoformo ao de trás)
        '''
        degrees_seq_1 = self.degree_sequence()
        g1 = self
        # Dicionário contendo o vértice e seu grau
        dict1 = {}
        for degree in degrees_seq_1:
            dict1[g1.node_with_a_degree(degree)] = degree
        
        print(dict1)

        degrees_seq_2 = G.degree_sequence()
        g2 = G
        # Dicionário contendo o vértice e seu grau
        dict2 = {}
        for degree in degrees_seq_2:
            dict2[g2.node_with_a_degree(degree)] = degree

        print(dict2)

        #Dicionário contendo o mapeamento dos nós/resposta final
        result = {}

        '''
        Etapas para detectar isomorfismo

            1. Checar se para cada nó existe um nó correspondente no outro grafo de mesmo grau

            2. Verificar se os vizinhos de ambos os nós possuem mesmo grau

            Em caso positivo, ambos os nós precisam sair da iteração, para não haver dois nós mapeados para um mesmo nó
        '''

        # Mapeando nós
        for node1 in dict1.items():
            for node2 in dict2.items():
                if node1[1] == node2[1] and node2[0] not in result.values():
                    result[node1[0]] = node2[0]
                    #Verificar os vizinhos
                    # ....


        print('\nResultado:')
        print(result)



        return True