# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 05:14:57 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""



# Georgian Calendar starts from 1582.


isLeap=False;
year=eval(input("Give the year"));
day=eval(input("Give the day of the First date of the year"));

if(year%4==0):
    isLeap=True;
    if(year%100==0):
        if(year%400==0):
            isLeap=True;
        else: 
            isLeap=False;
else: 
    isLeap=False;
    
    
monthDays=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
weekDays=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

if(isLeap):
    monthDays[1]=29;

for i in range(12):
    print(months[i], " 1", year, "is: ", weekDays[day%7]);
    day+=monthDays[i];      

          
          
          
          
          
          
          
          