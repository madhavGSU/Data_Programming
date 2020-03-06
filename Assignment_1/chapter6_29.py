'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''



def compressNumber(number):
	res=(number%10)+(number//10);
	return res;

def sumOfDoubleEvenPlace(str1):
	index=0;
	res=0;
	if(len(str1)%2==1):
		index=1;
	for i in range(index, len(str1), 2):
		digit=(ord(str1[i])-ord('0'));
		digit*=2;
		# print("index: ",i, " and digit: ", digit);
		if(digit>9):
			digit=compressNumber(digit);
		res+=digit;
	return res;




def sumOfOddPlace(str1):
	index=0; res=0;
	if(len(str1)%2==0):
		index+=1;

	for i in range(index, len(str1), 2):
		digit=(ord(str1[i])-ord('0'));
		res+=digit;
	return res;





def isValid(str1):

	sum1=sumOfDoubleEvenPlace(str1);
	sum2=sumOfOddPlace(str1);
	# print("even: ", sum1);
	# print("odd: ", sum2);
	total=sum1+sum2;
	if(total%10==0):
		return True;
	else:
		return False;




def main():

	str1=input("Enter the Credit Card Number: ");
	# print("Given input str: ", str1, " and len: ", len(str1));

	if(len(str1)<13 or len(str1)>16):
		print("1It is invalid");

	elif(str1[0]!='4' and str1[0,2]!="37" and str1[0]!='5' and str1[0]!='6'):
		print("It is invalid");
	else:
		if(isValid(str1)):
			print("It is valid.");
		else:
			print("It is invalid.");



main();