def read_file(file):
	file_read = open(file);
	return file_read.read();

def file_to_list(file):
	for ind,line in enumerate(file):
		file[ind] = line.split(';');
		for ind2, tupl in enumerate(file[ind]):
			file[ind][ind2] = tuple(tupl.split(','))
	return file;