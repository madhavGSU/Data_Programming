# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 03:26:52 2020

Author: Sai Madhav Kasam.
Data Programming Assignment 1.

"""

import random;


num1=random.randint(0,99);
num2=random.randint(0,99);
givenTotal=eval(input("What is "+str(num1)+" + "+str(num2)+"?"));
total=num1+num2;
print(total);
# givenTotal=eval(input("GIve the Total: "));
print("Correct answer.") if(total==givenTotal) else print("Wrong answer.");


