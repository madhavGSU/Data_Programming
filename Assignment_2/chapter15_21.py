'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



def binaryToDecimal(binaryString):
	res=0;

	for i in range(0, len(binaryString)):
		res*=2;
		res+=ord(binaryString[i])-ord('0');


	return res;







def main():

	str1=input("Give the binary string.");
	res=binaryToDecimal(str1);
	print("The decimal representation is: ", res);



main();