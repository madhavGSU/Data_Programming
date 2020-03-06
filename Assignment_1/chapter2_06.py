# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 04:33:25 2020

Author: Sai Madhav Kasam

Assignment-1.

"""

number=eval(input("Give the number"));
res=0;

while (number!=0):
    digit=number%10;
    res+=digit;
    number=number//10;
    
print("The result: ", res);