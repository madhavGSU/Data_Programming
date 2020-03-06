'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''



def binaryToHex(str1):

	res="";
	length=len(str1);
	val=0;
	included= 4 if(len(str1)%4==0) else len(str1)%4;
	for i in range(0, length):
		if(included==0):
			included=4;
			if(val<=9):
				res+=chr(val+48);
			else:
				res+=chr(val+87);
			val=0;
		val=val*2;
		val+=(ord(str1[i])-48);
		included-=1;

	if(val<=9):
		res+=chr(val+48);
	else:
		res+=chr(val+87);

	#print("result: ", res);
	return res;



def main():
	binaryValue=input("Give the binary format input.");
	print("The hexadecimal representation is:", binaryToHex(binaryValue));


main();