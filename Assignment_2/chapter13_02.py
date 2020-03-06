
'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''

import os;


def main():

	file=input("Give the filename: ");
	fileObj="";
	try:
		fileObj=open(file, "r");
	except:
		print("No such file exists.");
		return ;

	chars=0;
	words=0;
	lines=0;

	for line in fileObj:
		lines+=1;
		for word in line.split():
			# print(word, " ", end="");
			words+=1;
			chars+=len(word);


	fileObj.close();
	print(chars, " Characters");
	print(words, " Words.");
	print(lines, " lines.");


main();