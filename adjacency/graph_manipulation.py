from matrix_manipulation import create_adjacency
from matrix_manipulation import show_matrix
from matrix_manipulation import create_p
from matrix_manipulation import transpose
from matrix_manipulation import matrix_multiply
from matrix_manipulation import matrix_equals

from copy import deepcopy
import itertools
#import numpy as np
from numpy import array

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
	'''string = ''
	for i in list_int:
		string += '{};'.format(i)'''
	return [str(item) for item in list_int]

def recursive_unpacking(tup):
	if(isinstance(tup[0], int) and isinstance(tup[1], int)):
		return '{},{}'.format(tup[0],tup[1])
	else:
		return recursive_unpacking(tup[0]) + ',' + str(tup[1])

def tuples_to_list(permutations):
	final_permutations = []
	for ind, value in enumerate(permutations):
		final_permutations.append(recursive_unpacking(value))
		final_permutations[-1] = final_permutations[-1].split(',')
		final_permutations[-1] = [int(i) for i in final_permutations[-1]]

	return final_permutations

def remove_tuples(permutations, num_of_nodes):
	final_permutations = []
	for value in permutations:
		if(len(set(value)) == num_of_nodes):
			final_permutations.append(value)
	return final_permutations

def create_permutations(G):

	G_deg_seq = degree_sequence(G)
	first = nodes_with_degree(G, G_deg_seq[0])
	G_deg_seq.pop(0)

	while(len(G_deg_seq) > 0):
		second = nodes_with_degree(G, G_deg_seq[0])
		G_deg_seq.pop(0)
		first = itertools.product(first,second)

	permutations = tuples_to_list(first)

	permutations = remove_tuples(permutations, len(G))

	return permutations

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
	G_adj = array(create_adjacency(G, G_max_num+1))

	H_max_num = sorted(list(H.keys()))[-1]
	H_adj = array(create_adjacency(H, H_max_num+1))

	alphas = create_alphas(G, H)
	
	for alpha in alphas: # O(N!)
		P = array(create_p(alpha))
		P_trans = transpose(P)
		
		P_H_adj = matrix_multiply(P,H_adj)
		test_equals_G_adj = matrix_multiply(P_H_adj,P_trans)

		if(matrix_equals(G_adj, test_equals_G_adj)):
			#return alpha
			return True
	
	return False