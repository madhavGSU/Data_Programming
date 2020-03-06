# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 05:13:28 2020

Author: Sai Madhav Kasam
Data Programming Assignment-1.

"""

todayDate=eval(input("Enter today's day: "));
diffDates=eval(input("Enter the number of days since today: "));
newDay=(todayDate+diffDates)%7;

todayDay="a";
futureDay="a";
if(todayDate==0):
    todayDay="Sunday";
elif(todayDate==1):
    todayDay="Monday";
elif(todayDate==2):
    todayDay="Tuesday";
elif(todayDate==3):
    todayDay="Wednesday";
elif(todayDate==4):
    todayDay="Thursday";
elif(todayDate==5):
    todayDay="Friday";
elif(todayDate==6):
    todayDay="Saturday";


if(newDay==0):
    futureDay="Sunday";
elif(newDay==1):
    futureDay="Monday";
elif(newDay==2):
    futureDay="Tuesday";
elif(newDay==3):
    futureDay="Wednesday";
elif(newDay==4):
    futureDay="Thursday";
elif(newDay==5):
    futureDay="Friday";
elif(newDay==6):
    futureDay="Saturday";

print("Today is", todayDay, "and the future day is", futureDay);
    
