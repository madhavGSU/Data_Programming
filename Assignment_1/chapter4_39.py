# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:17:10 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""

import math;
import turtle;


firstCircleX=eval(input("Give the first circle x coordinate: "));
firstCircleY=eval(input("Give the first circle y coordinate: "));
firstCircleRadius=eval(input("Give the first Circle radius: "));

secondCircleX=eval(input("Give the second circle x coordinate: "));
secondCircleY=eval(input("Give the second circle y coordinate: "));
secondCircleRadius=eval(input("Give the second circle radius: "));

turtle.penup();
turtle.goto(firstCircleX, firstCircleY-firstCircleRadius);
turtle.pendown();
turtle.circle(firstCircleRadius);

turtle.penup();
turtle.goto(secondCircleX, secondCircleY-secondCircleRadius);
turtle.pendown();
turtle.circle(secondCircleRadius);
turtle.penup();

dist=math.sqrt(pow(firstCircleX-secondCircleX, 2)+pow(firstCircleY-secondCircleY, 2));
if(firstCircleRadius>secondCircleRadius and dist<=firstCircleRadius-secondCircleRadius):
    #print("Circle2 is inside Circle1");
    turtle.goto(firstCircleX, firstCircleY+firstCircleRadius);
    turtle.write("Circle2 is inside Circle1");
elif(secondCircleRadius>firstCircleRadius and dist<=secondCircleRadius-firstCircleRadius):
	# print("Circle1 is inside Circle2");
	turtle.goto(secondCircleX, secondCircleY+secondCircleRadius);
	turtle.write("Circle1 is inside Circle2");
elif(dist<firstCircleRadius+secondCircleRadius):
    #print("Circle2 overlaps Circle1");
    turtle.goto((firstCircleX+secondCircleX)/2, (firstCircleY+secondCircleY)/2);
    turtle.write("Circle2 overlaps Circle1");
else:
    #print("Circle2 does not overlap Circle1");
    turtle.goto(firstCircleX, firstCircleY-firstCircleRadius-30);
    turtle.write("Circle2 does not overlap Circle1");

turtle.done();