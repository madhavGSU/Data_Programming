# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 05:11:47 2020

Author: Sai Madhav Kasam
Data Programming Assignment-1.

"""

res=0;


for i in range(49):
    numer=2*i+1;
    denom=2*i+3;
    res+=(numer/denom);

print("res: ", res);