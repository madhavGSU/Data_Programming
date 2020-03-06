'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''




import os;


def main():

	# filePtr=open("testFile.txt", "w");
	# filePtr.write("Yo Bro 1\n");
	# filePtr.write("Yo Bro 2\n");
	# filePtr.write("Yo Bro 3\n");
	# filePtr.write("Yo Bro aaaaaaaaaaaaaaa4\n");
	# filePtr.close();

	# fileName="testFile.txt";
	fileName=input("Give the filename.");
	# print("filename is: ", fileName);
	try:
		fileObject=open(fileName, "r");
	except:
		print("No such filename exists.");
	dictWords={};
	for line in fileObject:
		for word in line.split():
			if word in dictWords:
				dictWords[word]+=1;
			else:
				dictWords[word]=1;			

	for key in dictWords.keys():
		print(key, "word occured", dictWords[key], "times.");
	fileObject.close();	


main();