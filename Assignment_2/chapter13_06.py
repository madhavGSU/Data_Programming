'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''

import os;


def main():


	fileName=input("Enter the file to be read: ");
	try: 
		fileObject=open(fileName, "r");
	except: 
		print("Such file doesn't exist.");
	wordsCount=0;
	for line in fileObject.readlines():
		for word in line.split():
			wordsCount+=1;
	print("The number of words: ", wordsCount);



main();