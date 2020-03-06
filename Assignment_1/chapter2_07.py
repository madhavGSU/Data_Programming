# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:56:14 2020

Author: Sai Madhav Kasam. 
Data Programming Assignment-1.


"""

minutes=eval(input("Give the minutes"));
minutesPerYear=60*24*365;
minutesPerDay=60*24;
years=minutes//minutesPerYear;
remMinutes=minutes%minutesPerYear;
days=remMinutes//minutesPerDay;
print(minutes, "minutes is approximately", years, "years and", days, "days.");