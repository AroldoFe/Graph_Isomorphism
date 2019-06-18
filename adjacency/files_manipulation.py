import os
''' 
	@Return a file read from some 'name.txt'
'''
def read_file():
	d = os.getcwd()
	d1 = os.path.join(d, "casos_teste")
	filename = input("Insira o nome do arquivo: ")
	file = os.path.join(d1, filename)
	read_file = open(file)
	return read_file.read();

'''
	@Param file is the string that contains all edges
	@Return Graph created by file
'''
def file_to_list(file):
	# Taking the string that represents the graph and spliting into edges
	file = file.split('\n')[0]
	file = file.split(';')
	
	# Taking each edge and turning into nodes
	nodes = []
	for node in file:
		node = node.split(',')
		nodes.append(int(node[0]))
		nodes.append(int(node[1]))
	# Removing duplicates
	nodes = list(set(nodes))
	
	# The dictionary will represent a adjacency list
	graph = {int(key):[] for key in nodes}
	
	# Adding wich nodes are adjacency
	for node in file:
		node = node.split(',')
		graph[int(node[0])].append(int(node[1]))
		graph[int(node[1])].append(int(node[0]))

	
	return graph

'''
	@Param alpha is de bijection
	@Return A string that contains the bijection f(G) = H
'''
def create_bijection(alpha):
	string = ''
	for i in range(len(alpha[0])):
		string += "f({}) = {}\n".format(alpha[0][i], alpha[1][i])
	return string

'''
	@Param g is the graph G
	@Param h is the graph H
	@Param are_isomo is a boolean the tells if g and h are isomorphic
	@Param alpha is the bijection
	@Return void Creates a file report showing G, H and alpha, if they are isomorphic
'''
def create_report(g, h, are_isomo, alpha):
	name_output = input("\nInsira nome do arquivo do relatório (digite .txt ao final do nome): ")
	file_result = open(name_output, "w")

	print('\n### RELATÓRIO DO EXPERIMENTO ###')

	print('graph G')
	file_result.write('graph G\n')
	print(g + '\n\n')
	file_result.write(g + '\n\n')

	print('graph H')
	file_result.write('graph H\n')
	print(h + '\n\n')
	file_result.write(h + '\n\n')

	if(are_isomo):
		print('G e H são isomorfos!\n')
		file_result.write('G e H são isomorfos!\n')
		print(create_bijection(alpha))
		file_result.write(create_bijection(alpha))
	else:
		print('G e H não são isomorfos!')
		file_result.write('G e H não são isomorfos!')

	file_result.close()