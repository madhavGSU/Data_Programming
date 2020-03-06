# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 07:19:11 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""


import turtle;
import math;
    

turtle.penup();
#turtle.goto(-315, 50*math.sin((-315/100)*2*math.pi));
turtle.goto(-405, 50*math.sin(math.radians(-405)));
turtle.pendown();  
turtle.color("red");

for x in range(-405, 406):
    #turtle.goto(x, 50*math.sin((x/100)*2*math.pi));
    turtle.goto(x, 50*math.sin(math.radians(x)));
    
    
turtle.penup();
turtle.goto(-405, 50*math.cos(math.radians(-405)));
turtle.pendown(); 
turtle.color("blue");
    
for x in range(-405, 406):
    #turtle.goto(x, 50*math.cos((x/100)*2*math.pi));
    turtle.goto(x, 50*math.cos(math.radians(x)));

    



############################Drawing the x and y axis on the graph.################################

turtle.penup();
turtle.goto(0, -100);
turtle.pendown();
turtle.color("black");
#turtle.left(90);
turtle.setheading(90);
turtle.forward(200);



turtle.penup();
turtle.goto(-410, 0);
turtle.pendown();
turtle.setheading(0);
#turtle.left(90);
turtle.forward(820);
    

#########################Writing the degree markings on the graph.###################################

turtle.penup();
turtle.goto(-180,-30);
turtle.pendown();
turtle.write("-TT");


turtle.penup();
turtle.goto(180,-30);
turtle.pendown();
turtle.write("TT");



turtle.penup();
turtle.goto(-360,-30);
turtle.pendown();
turtle.write("-2*TT");


turtle.penup();
turtle.goto(360,-30);
turtle.pendown();
turtle.write("2*TT");


turtle.done();