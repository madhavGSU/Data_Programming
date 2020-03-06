'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


def sumDigits(num):
	if(num==0):
		return 0;

	return num%10+sumDigits(num//10);





def main():

	num=eval(input("Give the ineger."));
	total=sumDigits(num);
	print("The sum of digits is: ", total);



main();