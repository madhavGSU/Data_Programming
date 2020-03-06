# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:38:37 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""

import math;


weight=eval(input("Input the weight in pounds"));
height=eval(input("Input the height in inches"));

weight=weight*0.45359237;
height=height*0.0254;

bmi=weight/(height**2);
bmi=round(bmi, 4);
print("BMI is: ", bmi);