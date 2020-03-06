'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''

def sumDigits(num):
	total=0;
	while(num!=0):
		total+=num%10;
		num//=10;

	return total;



def main():
	num=eval(input("Give the integer"));
	print("Sum of all digits in the number is:", sumDigits(num));



main();