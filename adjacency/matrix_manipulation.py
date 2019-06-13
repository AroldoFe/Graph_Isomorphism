import numpy as np

def create_adjacency(G, max_num):
	matrix = []
	for i in range(max_num):
		matrix.append([])
		for j in range(max_num):
			matrix[-1].append(0)

	for key, values in G.items():
		for value in values:
			matrix[key][value] = 1

	return matrix

def show_matrix(matrix):
	string = ''
	for line in matrix:
		for column in line:
			string += '{} '.format(column)
		string += '\n'
	return string

def create_p(alpha):
	matrix = []
	for i in range(len(alpha[0])):
		matrix.append([])
		for j in range(len(alpha[1])):
			matrix[-1].append(0)

	for i in alpha[0]:
		j = alpha[1][i]
		matrix[i][j] = 1
	
	return matrix

def transpose(matrix):
	return matrix.transpose()
	'''for j in range(len(matrix[0])): 
		linha = []
		for i in range(len(matrix)):
			linha.append(matrix[i][j])
		t_matrix.append(linha)
	
	return t_matrix'''

def matrix_multiply(A, B):
	return np.dot(A,B)
	'''result = []
				if(len(A[0]) != len(B)):
					return False
			
				for i in range(len(A)):
					result.append([])
					for j in range(len(B[0])):
						result[-1].append(0)
			
				for i in range(len(A)):
					for j in range(len(A[0])):
						val = 0
						for k in range(len(B[0])):
							val = val + A[i][k]*B[k][j]
						result[i][j] = val
				return result'''

def matrix_equals(A, B):
	a_shape = A.shape
	b_shape = B.shape
	if not(a_shape[0] != b_shape[0] or a_shape[1] != b_shape[1]):
		return False

	for i in range(len[A]):
		for j in range(len(A[0])):
			if(A[i][j] != B[i][j]):
				return False

	return True