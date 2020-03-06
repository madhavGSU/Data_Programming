# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 23:10:08 2020

Author: Sai Madhav Kasam

Assignment-1.

"""


subTotal=eval(input("Give the total amount."));
gratuityRate=eval(input("Give the gratuity rate"));

gratuity=(subTotal*gratuityRate)/100;
total=subTotal+gratuity;

print("The gratuity is: ", round(gratuity, 2));
print("The total is: ", round(total, 2));