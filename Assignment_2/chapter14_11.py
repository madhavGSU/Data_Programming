'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


import os;




def main():


	# fileName="testFile.txt";
	fileName=input("Give the filename.");
	# print("filename is: ", fileName);
	try:
		fileObject=open(fileName, "r");
	except:
		print("No such filename exists.");
		
	# print(fileObject.readlines());
	vowels={'A':0, 'E':0, 'I':0, 'O':0, 'U':0};
	totalChars=0;
	for line in fileObject:
		for word in line.split():
			# totalChars+=len(word);
			for i in range(len(word)):		
				if(word[i]>='a' and word[i]<='z'):
					totalChars+=1;
				if(word[i]>='A' and word[i]<='Z'):
					totalChars+=1;			


				if(word[i]=='a' or word[i]=='A'):
					vowels['A']+=1;
				elif(word[i]=='e' or word[i]=='E'):
					vowels['E']+=1;
				elif(word[i]=='i' or word[i]=='I'):
					vowels['I']+=1;
				elif(word[i]=='o' or word[i]=='O'):
					vowels['O']+=1;
				elif(word[i]=='u' or word[i]=='U'):
					vowels['U']+=1;

	totalVowels=vowels['A']+vowels['E']+vowels['I']+vowels['O']+vowels['U'];
	consonents=totalChars-totalVowels;
	print("Number of Vowels: ", totalVowels)
	print("Number of Consonents: ", consonents);
	fileObject.close();	


main();