# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 02:18:52 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""


res=0;
num=eval(input("Give the number"));

while(num!=0):
    digit=num%10;
    num//=10;
    res=res*10+digit;
    
print("The reversed number is", res);