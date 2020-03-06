# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:43:43 2020

Author: Sai Madhav Kasam
Data Programming Assignment 1.

"""

import turtle;

pointX=eval(input("Give the x coordinate center of the rectangle."));
pointY=eval(input("Give the y coordinate center of the rectangle."));



length=eval(input("Give the length"));
breadth=eval(input("Give the breadth"));

turtle.home();
turtle.penup();
turtle.goto(pointX,pointY-breadth//2);
turtle.pendown();

turtle.forward(length//2);
turtle.left(90);
turtle.forward(breadth);
turtle.left(90);
turtle.forward(length);
turtle.left(90);
turtle.forward(breadth);
turtle.left(90);
turtle.forward(length//2);
turtle.done();