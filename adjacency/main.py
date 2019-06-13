from files_manipulation import read_file
from files_manipulation import file_to_list
from graph_manipulation import are_isomorphic
from copy import deepcopy
import itertools

def main():
	arquivo1 = read_file();
	G = file_to_list(arquivo1)

	arquivo2 = read_file();
	H = file_to_list(arquivo2)

	if(are_isomorphic(G, H)):
		#write_file("result.txt", G, H, False)
		print("Os grafos são isomorfos!")
	else:
		#write_file("result.txt", G, H, True)
		print("Os grafos não são isomorfos!")

if __name__ == '__main__':
	main()