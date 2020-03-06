'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''

import math;



# def isPrime(number):
# 	if(number==2):
# 		return True;
# 	if(number%2==0):
# 		return False;
# 	cap=math.floor(math.sqrt(number));
# 	for i in range(3, cap+1):
# 		if(number%i==0):
# 			return False;
# 	return True;


def isPrime(number):
	divisor=2;
	while(divisor<=number/2):
		if(number%divisor==0):
			return False;
		divisor+=1;
	return True;





primes=0;
for i in range(2, 10001):
	if(isPrime(i)):
		primes+=1;

print("Number of prime numbers less than 10000 is: ", primes);