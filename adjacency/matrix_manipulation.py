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