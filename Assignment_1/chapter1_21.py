# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 04:22:35 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""


import turtle;


#print(turtle.pensize());
turtle.penup();
turtle.goto(0,-200);
turtle.pendown();

turtle.circle(200);
turtle.penup();
turtle.goto(193,0);
turtle.pendown();
turtle.write('3');

turtle.penup();
turtle.goto(0,-196);
turtle.pendown();
turtle.write('6');

turtle.penup();
turtle.goto(-193, 0);
turtle.pendown();
turtle.write('9');

turtle.penup();
turtle.goto(0,188);
turtle.pendown();
turtle.write('12');


turtle.penup();
turtle.goto(0,0);
turtle.pendown();
turtle.left(180);
turtle.width(5);
turtle.forward(75);

turtle.penup();
turtle.goto(0,0);
turtle.pendown();
turtle.right(180);
turtle.width(3)
turtle.forward(125);

turtle.penup();
turtle.goto(0,0);
turtle.pendown();
turtle.left(90);
turtle.width(1);
turtle.forward(175);

turtle.penup();
turtle.goto(-15,-215);
turtle.pendown();
turtle.write("9:15:00");

#turtle.hideturtle();

turtle.done();