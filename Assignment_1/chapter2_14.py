# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:16:08 2020

Author: Sai Madhav Kasam. 
Data Programming Assignment-1.

"""

import math;

point1X=eval(input("Give first point x coordinate"));
point1Y=eval(input("Give first point y coordinate"));


point2X=eval(input("Give second point x coordinate"));
point2Y=eval(input("Give second point y coordinate"));


point3X=eval(input("Give third point x coordinate"));
point3Y=eval(input("Give third point y coordinate"));


side1=math.sqrt((point1X-point2X)**2+ (point1Y-point2Y)**2);
# print("The side1 is: ", side1);
side2=math.sqrt((point3X-point2X)**2+ (point3Y-point2Y)**2);
# print("The side2 is: ", side2);
side3=math.sqrt((point1X-point3X)**2+ (point1Y-point3Y)**2);
# print("The side3 is: ", side3);
avg=(side1+side2+side3)/2;
# print("The avg is: ", avg);
# print("The temp is: ", avg*(avg-side1)*(avg-side2)*(avg-side3));

area=math.sqrt(avg*(avg-side1)*(avg-side2)*(avg-side3));
area=round(area, 2);
print("The area of the triangle is ", area);