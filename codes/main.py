from graph import Graph;
from files import file_to_list;
from files import read_file;
#import files;

graph1 = Graph()
file = file_to_list(read_file('grafos.txt').split('\n'))
graph1.add_edges(file[0])
#print(graph.nodes)
#print()
#print(graph.edges)
#print()
graph2 = Graph()
graph2.add_edges(file[1])
for key,value in graph1.nodes_edges.items():
	print("{}: {}".format(key, value))

print()

for key,value in graph2.nodes_edges.items():
	print("{}: {}".format(key, value))

print()
print(graph1.is_isomorphic(graph2))