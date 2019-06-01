from graph import Graph;
from files import read_file;

graph = Graph();
'''
graph.add_node(1)
graph.add_nodes([1,2,3,4])
graph.add_edges([(1,2),(2,1),(2,3),(4,1)])

print(graph.nodes_edges[1])
'''

file = read_file('grafos.txt').split('\n')
for ind,line in enumerate(file):
	file[ind] = line.split(';');
	for ind2, tupl in enumerate(file[ind]):
		file[ind][ind2] = tuple(tupl.split(','))

#print(file[0])

graph.add_edges(file[0])
print(graph.nodes)
print()
print(graph.edges)
print()
for key,value in graph.nodes_edges.items():
	print("{}: {}".format(key, value))