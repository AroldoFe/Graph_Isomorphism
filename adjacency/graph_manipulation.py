from matrix_manipulation import create_adjacency
from matrix_manipulation import show_matrix
from copy import deepcopy

def degree_seguence(G):
	return sorted([len(G[node]) for node in G.keys()], reverse=True)

def number_of_nodes(G):
	return len(G.keys())

def same_number_of_nodes(G, H):
	if(number_of_nodes(G) == number_of_nodes(H)):
		return True
	return False

def number_of_edges(G):
	n_edges = 0
	for value in G.values():
		n_edges += len(value)
	
	return n_edges/2;

def same_number_of_edges(G, H):
	if(number_of_edges(G) == number_of_edges(H)):
		return True
	return False

def degree_sequence(G):
	return sorted([len(value) for value in G.values()], reverse=True)

def same_degree_sequence(G, H):
	if(degree_seguence(G) == degree_sequence(H)):
		return True
	return False

def nodes_with_degree(G, degree):
	return [node for node in G if(len(G[node]) == degree)]

def all_to_str(list_int):
	string = ''
	for i in list_int:
		string += '{};'.format(i)
	return string

def create_permutation(first, second, f_degree, s_degree):
	if(f_degree != s_degree):
		for i in range(len(second)):
			first += ';'+first

	for i in range(len(second)):
		for item in first.split(';')[i]:
			if(item.split(',')[-1] != str(second[i])):
				first.split(';')[i] += ',{}'.format(second[i])

	return first
	'''permutation = []
	for i in range(len(second)):
		permutation.append(deepcopy(first))

	for i in range(len(second)):
		permutation[i].append(second[i]);
	print(permutation)
	return permutation'''


def create_permutations(G):

	G_deg_seq = degree_sequence(G)
	f_degree = G_deg_seq[0]
	first = all_to_str(nodes_with_degree(G, f_degree))
	G_deg_seq.pop(0)

	while(len(G_deg_seq) > 0):
		s_degree = G_deg_seq[0]
		second = nodes_with_degree(G, s_degree)
		G_deg_seq.pop(0)
		first = create_permutation(first, second, f_degree, s_degree)
		f_degree = s_degree

	print(first)

	return first

def create_alphas(G, H):
	alphas = []
	
	G_permutations = create_permutations(G)
	H_permutations = create_permutations(H)
	
	if(len(G_permutations) != len(H_permutations)):
		return False
	
	for G_permutation in G_permutations:
		for H_permutation in H_permutations:
			alphas.append((G_permutation, H_permutation))

	return alphas



def are_isomorphic(G, H):
	if not(same_number_of_nodes(G,H)):
		return False
	if not(same_number_of_edges(G, H)):
		return False
	if not(same_degree_sequence(G, H)):
		return False

	# Criar os alphas a partir das sequencias de graus

	G_max_num = sorted(list(G.keys()))[-1]
	G_adj = create_adjacency(G, G_max_num+1)

	H_max_num = sorted(list(H.keys()))[-1]
	H_adj = create_adjacency(H, H_max_num+1)

	alphas = create_alphas(G, H)

	#for alpha in alphas:
		#print(alpha)
	'''
	for alpha in alphas: # O(N!)
		P = create_p(alpha)
		P_trans = transpose(P)
		
		test_equals_G_adj = matrix_multiply(matrix_multiply(P,H_adj),P_trans)
		if(matrix_equals(G_adj, test_equals_G_adj)):
			return alpha
	'''
	return False