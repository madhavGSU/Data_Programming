# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 03:20:40 2020

@author: Administrator
"""

a=eval(input("Give the input for a: "));
b=eval(input("Give the input for b: "));
c=eval(input("Give the input for c: "));
d=eval(input("Give the input for d: "));
e=eval(input("Give the input for e: "));
f=eval(input("Give the input for f: "));

det=a*d-b*c;

if(det==0):
    print("The equation has no solution.");
else:
    x=(e*d-b*f)/det;
    y=(a*f-e*c)/det;
    print("x is", x, " and y is", y);

