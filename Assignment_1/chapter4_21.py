# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:16:48 2020

@author: Administrator
"""

year=eval(input("Enter the year: "));
month=eval(input("Enter the month with values between 1 and 12: "));
day=eval(input("Day of the month: "));
if(month<=2):
    month+=12;
    year-=1;

century=year//100;
yearOfCentury=year%100;

date=(day+((26*(month+1))//10)+(yearOfCentury)+(yearOfCentury//4)+(century//4)+(5*century))%7;

week=["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
print("Day of the week is", week[date]);