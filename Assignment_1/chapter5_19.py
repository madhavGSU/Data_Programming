# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:49:52 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""


rows=eval(input("Enter the number of lines from 1 to 15: "));


for i in range(1, rows+1):
    for j in range(0, rows-i):
        print(" \t", end="");
    for j in range(i,0,-1):
        print(j,"\t",  end="");
    for j in range(2,i+1):
        print(j,"", sep='\t', end="");

    print();


