# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:37:45 2020

@author: Administrator
"""

import math;

principal=eval(input("Give the principal amount"));
intRate=0.05/12;
# interest=principal*((1+(0.05)/12))**6;
interest=0;
total=principal;
for i in range(6):
	total=principal+interest;
	interest=total*(1+intRate);
	# print("account value after month", i, "is:", interest);

print("After the sixth month, the account value is:", round(interest, 2));
