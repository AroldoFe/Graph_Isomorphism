from graph import Graph;
from files import file_to_list;
from files import read_file;
import os
print('##### ISOMORFISMO DE GRAFOS APLICADOS A QUÍMICA #####\n')

print('# Este programa tem como objetivo avaliar se duas estruturas químicas são isomorfas ou não\n')

relatorio = []

d = os.getcwd()
d1 = os.path.join(d, "compostos")

nome_do_arquivo_1 = input("Insira nome do arquivo do grafo 1(incluindo o .txt): ")
fname1 = os.path.join(d1, nome_do_arquivo_1)

relatorio.append("RELATÓRIO")
relatorio.append("Arquivo do composto 1: ")
relatorio.append(fname1)

graph1 = Graph()
file = file_to_list(read_file(fname1).split('\n'))
graph1.add_edges(file[0])

print("\nLegenda dos grafos:")
print("Vértice: [Lista de arestas]\n")
print("GRAFO 1")
relatorio.append(' ')
relatorio.append("Legenda dos grafos:")
relatorio.append("Vértice: [Lista de arestas]")
relatorio.append("GRAFO 1")

for key,value in graph1.nodes_edges.items():
	print("{}: {}".format(key, value))
	string1 = "{}: {}".format(key, value)
	relatorio.append(string1)

print()

nome_do_arquivo_2 = input("Insira nome do arquivo do grafo 2(digite .txt ao final do nome): ")
fname2 = os.path.join(d1, nome_do_arquivo_2)

relatorio.append(' ')
relatorio.append("Arquivo do composto 2: ")
relatorio.append(fname2)

graph2 = Graph()
file = file_to_list(read_file(fname2).split('\n'))
graph2.add_edges(file[0])

print("\nGRAFO 2")
relatorio.append("GRAFO 2")
for key,value in graph2.nodes_edges.items():
	print("{}: {}".format(key, value))
	string2 = "{}: {}".format(key, value)
	relatorio.append(string2)

print()

resultado = graph1.is_isomorphic(graph2)

if resultado != False:
	relatorio.append(" ")
	relatorio.append("Resultado: ")

	for key, item in resultado.items():
		string3 = "{}: {}".format(key, item)
		relatorio.append(string3)

	nome_do_arquivo_de_output = input("\nInsira nome do arquivo do relatório (digite .txt ao final do nome): ")

	f = open(nome_do_arquivo_de_output, "x")
	f.close()

	f1 = open(nome_do_arquivo_de_output, "w")
	for item in relatorio:
		f1.write(item)
		f1.write("\n")
	f1.close()
else: 
	print ("## ESTRUTURAS SÃO DIFERENTES, COMPOSTOS NÃO SÃO ISOMORFOS")
	relatorio.append(" ")
	relatorio.append("## ESTRUTURAS SÃO DIFERENTES, COMPOSTOS NÃO SÃO ISOMORFOS")
	nome_do_arquivo_de_output = input("\nInsira nome do arquivo do relatório (digite .txt ao final do nome): ")

	f = open(nome_do_arquivo_de_output, "x")
	f.close()

	f1 = open(nome_do_arquivo_de_output, "w")
	for item in relatorio:
		f1.write(item)
		f1.write("\n")
	f1.close()




print("\n## RELATÓRIO CRIADO E PROGRAMA ENCERRADO ##")