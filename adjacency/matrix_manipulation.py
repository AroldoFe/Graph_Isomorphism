import numpy as np

'''
	@Param G is the adjacency list that will be turn into a adjacency matrix
	@Return the adjacency matrix created from adjacency list
	@Complexity O(N^2)
'''
def create_adjacency(G):
	matrix = np.zeros((len(G),len(G)))

	for key, values in G.items():
		for value in values:
			matrix[key][value] = 1

	return matrix

'''
	@Param matrix that will be turn into a string
	@Return string that shows tha matrix
	@Complexity O(N^2)
'''
def show_matrix(matrix):
	string = ''
	for line in matrix:
		for column in line:
			string += '{} '.format(column)
		string += '\n'
	return string

'''
	@Param alpha is the bijection that will be turn into matrix
	@Return the matrix
	@Complexity O(N^2)
'''
def create_p(alpha):
	matrix = np.zeros((len(alpha[0]),len(alpha[0])))

	for i in range(len(alpha[0])):
		matrix[alpha[0][i]][alpha[1][i]] = 1
	
	return matrix

'''
	@Param matrix that will be transposed
	@Return the transposed matrix
	@Complexity O(N^2)
'''
def transpose(matrix):
	return matrix.transpose()

'''
	@Param A matrix A
	@Param B matrix B
	@Return AxB
	@Complexity O(N^3)
'''
def matrix_multiply(A, B):
	return np.dot(A,B)

'''
	@Param A matrix A
	@Param B matrix B
	@Return True if A = B
	@Complexity O(N^2)
'''
def matrix_equals(A, B):
	a_shape = A.shape
	b_shape = B.shape

	if(a_shape[0] != b_shape[0] or a_shape[1] != b_shape[1]):
		return False

	for i in range(a_shape[0]):
		for j in range(a_shape[1]):
			if(A[i][j] != B[i][j]):
				return False

	return True