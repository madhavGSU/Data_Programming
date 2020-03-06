'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''





def main():


	# filePtr=open("testFile3.txt", "w");
	# filePtr.write("Write a program that removes all the occurrences of a string from a file.\n");
	# filePtr.write("Your program should prompt user to enter a filename\n");
	# filePtr.write("and a string to be removed. Below is a sample run.\n")
	# filePtr.close();


	fileName=input("Give the name of the file to be scanned: ");
	removeWord=input("Give the word to be removed from the file: ");

	fileObj=open(fileName, "r");
	
	res="";
	for line in fileObj.readlines():
		# print(line);
		if(len(line)==0):
			continue;
		# fileObj2.write("abcd\n");
		for word in line.split():
			if(word!=removeWord):
				res+=word+" ";
		res=res[:-1];
		res+="\n";


	fileObj2=open(fileName, "w");
	fileObj2.write(res);


	fileObj.close();
	fileObj2.close();
	print("Done");




main();