'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



def gcd(num1, num2):

	if(num1%num2==0):
		return num2;

	return gcd(num2, num1%num2);





def main():
	num1=eval(input("Give the first digit."));
	num2=eval(input("Give the second digit."));
	res=gcd(num1, num2);
	print("The gcd of two numbers is: ", res);





main();