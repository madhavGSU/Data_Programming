'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


def isValidPassword(str1):
	if(len(str1)<8):
		return False;

	if(not str1.isalnum()):
		return False;
	digits=0;
	for ch in str1:
		if(ch>='0' and ch<='9'):
			digits+=1;
	if(digits<2):
		return False;
	return True;







def main():
	str1=input("Enter the password to be verified.");
	if(isValidPassword(str1)):
		print("Valid password.");
	else:
		print("Invalid password.");


main();