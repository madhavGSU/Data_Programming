'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


import math;


def displaySortedNumbers(num1, num2, num3):
	max1=max(num1, num2);
	max2=min(num1, num2);
	max3=-1;
	if(num3>=max1):
		max3=max2;
		max2=max1;
		max1=num3;
	elif(num3>=max2):
		max3=max2;
		max2=num3;
	else:
		max3=num3;
	print("The sorted numbers are: ", max3, max2, max1);






num1, num2, num3=eval(input("Enter three numbers: "));
# num2=eval(input("Give the number2: "));
# num3=eval(input("Give the number3: "));
displaySortedNumbers(num1, num2, num3);