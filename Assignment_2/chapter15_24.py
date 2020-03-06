'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


import os;


def filesCount(path):
	res=0;
	rep=os.scandir(path);

	for entry in rep:
		if(not os.path.isfile(entry)):

			res+=filesCount(entry);
		else:
			# print(entry.name);
			res+=1;
	return res;







def main():
	path=input("Give the file address.");
	try:
		res=filesCount(path);
		print("Number of files in the directory is: ", res);
	except:
		print("Such directory doesn't exist");



main();