# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:24:46 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""

num1=eval(input("Give the first number"));
num2=eval(input("Give the second number"));


minm=min(num1, num2);
# maxm=max(num1, num2);

for i in range(minm, 0, -1):
    if(num1%i==0 and num2%i==0):
        print("GCD is: ", i);
        break;


