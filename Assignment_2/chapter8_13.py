
def longestCommonPrefix(str1, str2):

	res="";
	index=0;

	while(index<len(str1) and index<len(str2)):
		if(str1[index]==str2[index]):
			res+=str1[index];
		else:
			break;
		index+=1;

	return res;



def main():
	str1=input("Enter the first string.");
	str2=input("Enter the second string.");
	print("The longest common prefix of both strings is: ", longestCommonPrefix(str1, str2));



main();