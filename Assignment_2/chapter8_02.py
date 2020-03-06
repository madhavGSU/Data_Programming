'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''



def isSubstring(str1, str2, index2):
	index1=0;
	while(index1<len(str1) and index2<len(str2)):
		#print("comparing chars: ", str1[index1], "second char: ", str2[index2]);
		if(str1[index1]!=str2[index2]):
			return False;
		index1+=1;
		index2+=1;
	return True;



def find(str1, str2):
	if(len(str1)>len(str2)):
		return False;
	else:
		for i in range(0, len(str2)-len(str1)+1):
			#print("start index is: ", i);
			if(isSubstring(str1, str2, i)):
				return True;
		return False;




def main():
	str1=input("Give the first string.");
	str2=input("Give the second string.");
	if(find(str1, str2)):
		print("It is substring");
	else:
		print("It is not substring.");



main();