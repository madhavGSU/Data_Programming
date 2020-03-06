'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


import math;


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





def isPrime(number):
	if(number==2):
		return True;
	if(number%2==0):
		return False;
	cap=math.floor(math.sqrt(number));
	for i in range(3, cap+1):
		if(number%i==0):
			return False;
	return True;



primes=0;
number=2;
while(primes<100):

	if(isPalindrome(number)==False or isPrime(number)==False):
		number+=1;
		continue;
	
	primes+=1;
	print(number,"\t", end="");
	#print('{:010d}'.format(number), sep="\t", end="");
	if(primes>0 and primes%10==0):
		print("");

	number+=1;



