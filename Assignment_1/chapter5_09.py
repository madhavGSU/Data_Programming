# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:13:16 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""

import math;




amount=10000;
tuition=0;

tuition=amount*pow((1+0.05), 10);
print("finalAmount: ", tuition);



res=tuition;        # First Year.
tuition*=1.05;
res+=tuition;       # Second Year.
tuition*=1.05;
res+=tuition;       # Third Year.
tuition*=1.05;
res+=tuition;       # Fourth Year.
print("Total fees is:", round(res, 2));