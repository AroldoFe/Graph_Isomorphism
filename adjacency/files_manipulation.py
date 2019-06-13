def read_file():
	file = input("Insira o nome do arquivo: ")
	read_file = open(file)
	return read_file.read();

def file_to_list(file):
	# Pegando a string do grafo
	file = file.split('\n')[0]
	# Separando por arestas
	file = file.split(';')
	
	nodes = []
	for node in file:
		node = node.split(',')
		nodes.append(int(node[0]))
		nodes.append(int(node[1]))
	nodes = list(set(nodes))
	
	# Quero montar um dicionario que seja equivalente a lista de adjacencia
	grafo = {int(key):[] for key in nodes}
	
	for node in file:
		node = node.split(',')
		grafo[int(node[0])].append(int(node[1]))
		grafo[int(node[1])].append(int(node[0]))

	return grafo