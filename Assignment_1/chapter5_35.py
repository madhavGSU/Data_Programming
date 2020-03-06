# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 06:22:32 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""

import math;


for i in range(2, 10000):
    total=0;
    cap=math.floor(math.sqrt(i));
    #print("i:", i, " cap: ", cap);
    for j in range(1, cap+1):
        if(i%j!=0): 
            continue;
        num=i//j;
        total+=j;
        if(num!=j and num!=i): 
            total+=num;
    #print("i: ",i," total: ", total);
    if(total==i):
        print("Found perfect number: ", i);