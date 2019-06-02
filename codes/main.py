from graph import Graph;
import files;

graph = Graph()

file = file_to_list(read_file('grafos.txt').split('\n'))

graph.add_edges(file[0])
print(graph.nodes)
print()
print(graph.edges)
print()
for key,value in graph.nodes_edges.items():
	print("{}: {}".format(key, value))