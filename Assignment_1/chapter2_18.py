# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:43:08 2020

@author: Administrator
"""

import math;
import datetime;
import time;


#offset=eval(input("Enter the time zone offset to GMT: "));

#print("The time is: ", datetime.datetime.utcnow());


#currTime=datetime.datetime.now();
#print(currTime);
#newTime=currTime-datetime.timedelta(hours=-5)
#print(newTime);


currTime=time.time();
# print(currTime);
totalSeconds=int(currTime);

currentSeconds=totalSeconds%60;
totalMinutes=totalSeconds//60;

currentMinutes=totalMinutes%60;
totalHours=totalMinutes//60;

currentHours=totalHours%24;

offset=eval(input("Enter the time zone offset to GMT: "));

newHours=(currentHours+offset)%24;

print("The current time is: ", newHours,":", currentMinutes,":", currentSeconds, sep="");


