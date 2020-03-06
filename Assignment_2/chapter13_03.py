'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


import os;


def main():


	# filePtr=open("testFile2.txt", "w");
	# filePtr.write("20 30 40\n");
	# filePtr.write("30 40 50 20 110 230.5\n");
	# filePtr.write("40 50 60 70\n");
	# filePtr.close();

	file=input("Give the filename: ");
	fileObj="";
	try:
		fileObj=open(file, "r");
	except:
		print("No such file exists.");
		return ;

	scores=0;
	totalScore=0.0;

	line=fileObj.readline();
	while(line):
		# print(line);
		for num in line.split():
			totalScore+=eval(num);
			scores+=1;
		line=fileObj.readline();

	fileObj.close();
	print("There are", scores, "scores");
	print("The total is", totalScore);
	print("The average is", round(totalScore/scores,2));


	# for line in fileObj:
	# 	lines+=1;
	# 	for word in line.split():
	# 		# print(word, " ", end="");
	# 		words+=1;
	# 		chars+=len(word);


	# print(chars, " Characters");
	# print(words, " Words.");
	# print(lines, " lines.");


main();