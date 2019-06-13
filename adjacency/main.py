from files_manipulation import read_file
from files_manipulation import file_to_list
from graph_manipulation import are_isomorphic
from copy import deepcopy
import itertools

def main():

	relatorio = []
	relatorio.append("GRAFO 1")
	arquivo1 = read_file();
	relatorio.append(arquivo1)
	G = file_to_list(arquivo1)

	relatorio.append(" ")
	relatorio.append("GRAFO 2")
	arquivo2 = read_file();
	relatorio.append(arquivo2)
	H = file_to_list(arquivo2)

	relatorio.append(" ")

	if(are_isomorphic(G, H)):
		#write_file("result.txt", G, H, False)
		print("Os grafos são isomorfos!")
		relatorio.append("Os grafos são isomorfos!")
	else:
		#write_file("result.txt", G, H, True)
		print("Os grafos não são isomorfos!")
		relatorio.append("Os grafos não são isomorfos!")

	nome_do_arquivo_de_output = input("\nInsira nome do arquivo do relatório (digite .txt ao final do nome): ")

	f = open(nome_do_arquivo_de_output, "x")
	f.close()

	f1 = open(nome_do_arquivo_de_output, "w")
	for item in relatorio:
		f1.write(item)
		f1.write("\n")
	f1.close()

if __name__ == '__main__':
	main()