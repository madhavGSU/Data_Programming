'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


def count(str1):
	res=0;

	for c in str1:
		if(c.isalpha()):
			res+=1;
	return res;



def main():
	str1=input("Enter the string.");
	print("Number of letters in the string are: ", count(str1));


main();