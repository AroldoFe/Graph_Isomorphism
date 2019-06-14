import files_manipulation as fm
import graph_manipulation as gm

'''
	@Author Aroldo Felix
	@Author Gabriel Igor
	@Date 2019-06-01 (YYYY-MM-DD)
	@Last Update 2019-06-14 (YYYY-MM-DD)
'''
def main():
	# Read the first file and turn into a adjacency list
	grafo_g = fm.read_file();
	G = fm.file_to_list(grafo_g)

	# Read the second file and turn into a adjacency list
	grafo_h = fm.read_file();
	H = fm.file_to_list(grafo_h)

	# Test if they are isomorphic
	answer_isomorphism, alpha = gm.are_isomorphic(G,H)

	# Write a file that contains the answer
	fm.create_report(grafo_g, grafo_h, answer_isomorphism, alpha)

if __name__ == '__main__':
	main()