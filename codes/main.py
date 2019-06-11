from graph import Graph;
from files import file_to_list;
from files import read_file;
#import files;
print('##### ISOMORFISMO DE GRAFOS APLICADOS A QUÍMICA #####\n')

print('# Este programa tem como objetivo avaliar se duas estruturas químicas são isomorfas\n')

graph1 = Graph()
arq1 = input("Insira nome do arquivo do grafo 1: ")
file = file_to_list(read_file(arq1).split('\n'))
graph1.add_edges(file[0])

for key,value in graph1.nodes_edges.items():
	print("{}: {}".format(key, value))

print()

graph2 = Graph()
arq2 = input("Insira nome do arquivo do grafo 2: ")
file = file_to_list(read_file(arq2).split('\n'))
graph2.add_edges(file[0])

for key,value in graph2.nodes_edges.items():
	print("{}: {}".format(key, value))

print()

print(graph1.is_isomorphic(graph2))
