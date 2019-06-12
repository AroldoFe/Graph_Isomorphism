# @Param nodes é um conjunto de Vértices
# @Param edges é um conjunto de arestas, ou seja, tuplas de Vértices

from copy import deepcopy

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

        '''
            Estratégia de Isomorfismo de grafos
            * Pode fazer um dicionario de vértice com seus vértices adjacentes
            * Tentar projetar um vértice no de mesmo grau e fazer com seus adjacentes

            * Tentar ligar dois grafos por arestas de modo que todo vértice de um grafo G deve estar ligado a exatamente um vértice de H
            * Se existe algum nó de G que não está ligado a H, então não são isomorfos
            * dois vértices x,y serão "isomorfos" se existe ciclo de tamanho 4 passando por 2 arestas de ligação de grafos para todas as arestas de x (exemplo de cubo que o plano da frente é isomoformo ao de trás)
        '''
        
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


            Etapas para detectar isomorfismo

                1. Checar se para cada nó existe um nó correspondente no outro grafo de mesmo grau

                2. Verificar se os vizinhos de ambos os nós possuem mesmo grau

                Em caso positivo, ambos os nós precisam sair da iteração, para não haver dois nós mapeados para um mesmo nó
            

            # Mapeando nós
            for node1 in dict1.items():
                for node2 in dict2.items():
                    if node1[1] == node2[1] and node2[0] not in result.values():
                        result[node1[0]] = node2[0]
                        #Verificar os vizinhos
                        # ....
        '''

        '''
            # Desenvolvimento: GABRIEL
            G_copy = deepcopy(self)
            H_copy = deepcopy(G)

            # Conferindo se o grafo realmente foi copiado
            #for key,value in G_copy.nodes_edges.items():
            #    print("{}: {}".format(key, value))
            
            
            # Pegar vértices de maior grau
            v1 = G_copy.highest_degree_node()
            v2 = H_copy.highest_degree_node()


            nodes_bijection = [(v1,v2)]        
            while(len(nodes_bijection) != len(self.nodes)):
                if len(G_copy.neighbors_nodes(v1)) == len(H_copy.neighbors_nodes(v2)):
                    G_copy.rem_node(v1)
                    H_copy.rem_node(v2)
        '''
        
        
        # Desenvolvimento: AROLDO
        # O mapeamento pode ser obtido por um vetor de tamanho len(self.nodes) com tuplas de vértices de G projetados em vértices de H

        G_copy = deepcopy(self)
        H_copy = deepcopy(H)

        visited = {'G':[],'H':[]}
        non_visited = {'G':G_copy.nodes, 'H':H_copy.nodes}
        nodes_bijection = []
        nodes_possibles_bijection = []

        # pegas os nós de mesmo grau dado um grau
        G_highest_nodes_degrees, H_highest_nodes_degrees = G_copy.init_highest_degree(H_copy)

        # Fazendo combinação de quais nós podem se combinar com quais
        for G_node in G_highest_nodes_degrees:
            for H_node in H_highest_nodes_degrees:
                nodes_possibles_bijection.append((G_node,H_node))

        #nodes_bijection.append(nodes_possibles_bijection[0])
        #nodes_possibles_bijection.pop(0)

        #
        for pack in nodes_possibles_bijection:
            v1 = pack[0]
            v2 = pack[1]
            # Listas contenco nós adjacentes a v1, v2 respectivamente
            v1_neighbors = G_copy.neighbors_nodes(v1)
            v2_neighbors = H_copy.neighbors_nodes(v2)
            # sequencias de graus
            v1_neighbors_degree = sorted([len(G_copy.nodes_edges[key]) for key in v1_neighbors], reverse=True)
            v2_neighbors_degree = sorted([len(H_copy.nodes_edges[key]) for key in v2_neighbors], reverse=True)
            # Essas sequencias são iguais
            iguais = True
            for i in range(len(v1_neighbors_degree)):
                if(v1_neighbors_degree[i] != v2_neighbors_degree[i]):
                    iguais = False
                    break;

            if not(iguais):
                continue

            # Se forem iguais começa a fazer a bijeção
            nodes_bijection.append(pack);
            



        '''
            # Pegar vértices de maior grau
            v1 = G_copy.highest_degree_node()
            v2 = H_copy.highest_degree_node()
        
            # Se tiverem mesma quantidade de adjacentes, qual o vetor de grau dos filhos?
            while(len(nodes_bijection) != len(self.nodes)):
                # 1) v1 tem mesma quantidade de descendentes que v2? Se sim, pego os adjacentes a v1 e v2 e removo v1 e v2 dos grafos
                if len(G_copy.neighbors_nodes(v1)) == len(H_copy.neighbors_nodes(v2)):
                    adj1 = G_copy.neighbors_nodes(v1)
                    adj2 = H_copy.neighbors_nodes(v2)
                    G_copy.rem_node(v1)
                    H_copy.rem_node(v2)
                # 2) Qual filho de v1 tem mais descendentes? Qual o filho de v2 tem mais descendentes?
                    v1_son = G_copy.highest_degree_node_from_list(adj1)
                    v2_son = H_copy.highest_degree_node_from_list(adj2)
                # 3) Estes têm mesma quantidade de descendentes? Se sim, repete o passo 1. Se não
                    if len(G_copy.neighbors_nodes(v1_son)) == len(H_copy.neighbors_nodes(v2_son)):

            print('\nResultado: {}'.format(result))
            #print(result)
        
        '''

        return True