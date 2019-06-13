from files_manipulation import read_file
from files_manipulation import file_to_list
from graph_manipulation import are_isomorphic
from copy import deepcopy
def main():
	arquivo1 = read_file();
	G = file_to_list(arquivo1)

	arquivo2 = read_file();
	H = file_to_list(arquivo2)

	if not(are_isomorphic(G, H)):
		#write_file("result.txt", G, H, False)
		print("Os grafos não são isomorfos!")
	else:
		#write_file("result.txt", G, H, True)
		print("Os grafos são isomorfos!")

if __name__ == '__main__':
	'''list1 = [1,2]
	list2 = [3,4]
	permutation = []
	for i in range(len(list2)):
		permutation.append(deepcopy(list1))
	print(permutation)
	
	#for ind, value in enumerate(permutation):
		#print(ind, value.append(list2[ind]))
		#permutation[ind].append(list2[ind])


	for i in range(len(list2)):
		print(i, permutation[i], list2[i])
		permutation[i].append(list2[i]);

	print(permutation)'''
	main()
