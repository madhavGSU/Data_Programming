# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 03:10:29 2020

@author: Administrator
"""


import turtle;


point1X=eval(input("Give the x coordinate of first point"));
point1Y=eval(input("Give the y coordinate of first point"));


point2X=eval(input("Give the x coordinate of second point"));
point2Y=eval(input("Give the y coordinate of second point"));


turtle.penup();
turtle.goto(point1X, point1Y);
turtle.pendown();
turtle.write("("+str(point1X)+","+str(point1Y)+")");


turtle.goto(point2X, point2Y);
turtle.write("("+str(point2X)+","+str(point2Y)+")");


"""

turtle.right(72);
turtle.forward(length);

turtle.right(144);
turtle.forward(length);


turtle.right(144);
turtle.forward(length);

turtle.right(144);
turtle.forward(length);


turtle.right(144);
turtle.forward(length);
"""

turtle.done();

