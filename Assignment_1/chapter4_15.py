# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 05:23:56 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""

import random;
import math;



randNumber=random.randint(100, 999);
# temp=randNumber;
thirdDigit=randNumber%10;
randNumber//=10;
secondDigit=randNumber%10;
randNumber//=10;
firstDigit=randNumber;


guessNumber=eval(input("Give a random 3 digit number: "));
# print("Generated random number is: ", temp);
guessedThirdDigit=guessNumber%10;
guessNumber//=10;
guessedSecondDigit=guessNumber%10;
guessNumber//=10;
guessedFirstDigit=guessNumber;


prize=0;
if(guessNumber==randNumber):
	prize=10000;
elif((thirdDigit==guessedThirdDigit and secondDigit==guessedFirstDigit and firstDigit==guessedSecondDigit)
	or (thirdDigit==guessedSecondDigit and secondDigit==guessedFirstDigit and firstDigit==guessedThirdDigit)
	or (thirdDigit==guessedSecondDigit and secondDigit==guessedThirdDigit and firstDigit==guessedFirstDigit)
	or (thirdDigit==guessedFirstDigit and secondDigit==guessedThirdDigit and firstDigit==guessedSecondDigit)
	or (thirdDigit==guessedFirstDigit and secondDigit==guessedSecondDigit and firstDigit==guessedThirdDigit)):
	prize=3000;
elif((thirdDigit==guessedFirstDigit or thirdDigit==guessedSecondDigit or thirdDigit==guessedThirdDigit) 
	or (secondDigit==guessedFirstDigit or secondDigit==guessedSecondDigit or secondDigit==guessedThirdDigit) 
	or (firstDigit==guessedFirstDigit or firstDigit==guessedSecondDigit or firstDigit==guessedThirdDigit)):
	prize=1000;

print("The prize money is: ", prize);