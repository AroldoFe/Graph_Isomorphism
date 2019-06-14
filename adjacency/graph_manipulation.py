import matrix_manipulation as mm
# This library is used to create permutations
import itertools

'''
	@Param G is a graph
	@Return the number of nodes in G
	@Complexity O(N)
'''
def number_of_nodes(G):
	return len(G.keys())

'''
	@Param G is a graph
	@Param H is a graph
	@Return True if G and H have the same number of nodes
	@Complexity O(N)
'''
def same_number_of_nodes(G, H):
	if(number_of_nodes(G) == number_of_nodes(H)):
		return True
	return False

'''
	@Param G is a graph
	@Return the number of edges in G
	@Complexity O(E)
'''
def number_of_edges(G):
	n_edges = 0
	for value in G.values():
		n_edges += len(value)
	
	return n_edges/2;

'''
	@Param G is a graph
	@Param H is a graph
	@Return True if G and H have the same number of nodes
	@Complexity O(E)
'''
def same_number_of_edges(G, H):
	if(number_of_edges(G) == number_of_edges(H)):
		return True
	return False

'''
	@Param G is a graph
	@Return the non increasing degree sequence of G
	@Complexity O(N^2)
'''
def degree_sequence(G):
	return sorted([len(node) for node in G.values()], reverse=True)

'''
	@Param G is a graph
	@Param H is a graph
	@Return True if G and H have the same non increasing degree sequence
	@Complexity O(N^2)
'''
def same_degree_sequence(G, H):
	if(degree_seguence(G) == degree_sequence(H)):
		return True
	return False

'''
	@Param G is a graph
	@Param degree is the degree
	@Return nodes with this degree
	@Complexity O(N^2)
'''
def nodes_with_degree(G, degree):
	return [node for node in G if(len(G[node]) == degree)]

'''
	@Param list_int is a list of integers
	@Return list of strings instead of integers
	@Complexity O(|list_int|)
'''
def all_to_str(list_int):
	return [str(item) for item in list_int]

'''
	@Param tup is a tuple
	@Return the string that contains the unpacking of a tuple
	@Complexity O(N)
'''
def recursive_unpacking(tup):
	if(isinstance(tup[0], int) and isinstance(tup[1], int)):
		return '{},{}'.format(tup[0],tup[1])
	else:
		return recursive_unpacking(tup[0]) + ',' + str(tup[1])

'''
	@Param permutations all permutations of nodes
	@Return list of permutations with int
	@Complexity O(N!)
'''
def tuples_to_list(permutations):
	final_permutations = []
	for ind, value in enumerate(permutations):
		final_permutations.append(recursive_unpacking(value))
		final_permutations[-1] = final_permutations[-1].split(',')
		final_permutations[-1] = [int(i) for i in final_permutations[-1]]

	return final_permutations

'''
	@Param permutations all permutations
	@Param num_of_nodes the number of nodes in G
	@Return only the permutations that has num_of_nodes non repeated items
	@Complexity O(N!)
'''
def remove_tuples(permutations, num_of_nodes):
	final_permutations = []
	for value in permutations:
		if(len(set(value)) == num_of_nodes):
			final_permutations.append(value)
	return final_permutations

'''
	@Param G is a graph
	@Return The valids permutations of nodes
	@Complexity O(N!)
'''
def create_permutations(G):

	G_deg_seq = degree_sequence(G) #O(N^2)
	first = nodes_with_degree(G, G_deg_seq[0]) #O(N^2)
	G_deg_seq.pop(0)

	while(len(G_deg_seq) > 0): #O(N)
		second = nodes_with_degree(G, G_deg_seq[0]) #O(N^2)
		G_deg_seq.pop(0)
		first = itertools.product(first,second) #O(N^2)

	permutations = tuples_to_list(first) #O(N!)

	permutations = remove_tuples(permutations, len(G)) #O(N!)

	return permutations

'''
	@Param G is a graph
	@Param H is a graph
	@Return return tuples of all possibles permutations betwen G and H nodes
	@Complexity (N!^2)
'''
def create_alphas(G, H):
	alphas = []
	
	G_permutations = create_permutations(G) #O(N!)
	H_permutations = create_permutations(H)
	
	if(len(G_permutations) != len(H_permutations)):
		return False
	
	for G_permutation in G_permutations: #O(N!)
		for H_permutation in H_permutations: #O(N!)
			alphas.append((G_permutation, H_permutation))

	return alphas

'''
	@Param G is a graph
	@Param H is a graph
	@Return True if G and H are isomorphic 
	@Return the bijection betwen G and H
	@Complexity O(N!^2 * N^3)
'''
def are_isomorphic(G, H):
	if not(same_number_of_nodes(G,H)): #O(N^2)
		return False, None
	if not(same_number_of_edges(G, H)): #O(N^2)
		return False, None
	if not(same_degree_sequence(G, H)): #O(N^2)
		return False, None

	# Create alphas from degree sequence
	alphas = create_alphas(G, H) # O(N!^2)

	G_adj = mm.create_adjacency(G) #O(N^2)
	H_adj = mm.create_adjacency(H)

	for alpha in alphas: # O(N!^2)
		P = mm.create_p(alpha) # O(N^2)
		P_trans = mm.transpose(P) # O(N^2)
	
		P_H_adj = mm.matrix_multiply(P,H_adj) #O(N^3)
	
		test_equals_G_adj = mm.matrix_multiply(P_H_adj,P_trans) #O(N^3)

		if(mm.matrix_equals(G_adj, test_equals_G_adj)): #O(N^2)
			return True, alpha

	return False, None