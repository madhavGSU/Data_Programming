'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''



def reverse(number):
	res=0;
	while(number!=0):
		res=res*10+number%10;
		number//=10;
	return res;


def isPalindrome(number):
	revNumber=reverse(number);
	# str1=str(number);
	# str2=str(revNumber);
	# if(len(str1)!=len(str2)):
	# 	return False;
	# for i in range(len(str1)):
	# 	ch1=str1[i];
	# 	ch2=str2[i];
	# 	if(ch1!=ch2): 
	# 		return False;
	# return True;
	return (number==revNumber);



def main():

	number=eval(input("Give the number"));
	if(isPalindrome(number)):
		print("The number is palindrome.");
	else:
		print("It's not a palindrome.");


main();