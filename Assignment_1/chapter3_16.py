# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 02:27:09 2020

@author: Administrator
"""

import turtle;


#turtle.showturtle();


length=eval(input("Give the length of the star"));

#turtle.circle(200, steps=3);


### Triangle.
turtle.penup();
turtle.goto(-3*length,-200);
turtle.pendown();


turtle.forward(length);
turtle.left(120);

turtle.forward(length);
turtle.left(120);

turtle.forward(length);
turtle.left(120);


### Rectangle.



turtle.penup();
turtle.goto(-1.75*length,-200);
turtle.pendown();


turtle.forward(length);
turtle.left(90);

turtle.forward(length);
turtle.left(90);

turtle.forward(length);
turtle.left(90);

turtle.forward(length);
turtle.left(90);




### Pentagon.


turtle.penup();
turtle.goto(0,-200);
turtle.pendown();


turtle.forward(length);
turtle.left(72);

turtle.forward(length);
turtle.left(72);

turtle.forward(length);
turtle.left(72);

turtle.forward(length);
turtle.left(72);

turtle.forward(length);
turtle.left(72);



### Hexgaon.


turtle.penup();
turtle.goto(2*length,-200);
turtle.pendown();


turtle.forward(length);
turtle.left(60);

turtle.forward(length);
turtle.left(60);

turtle.forward(length);
turtle.left(60);

turtle.forward(length);
turtle.left(60);

turtle.forward(length);
turtle.left(60);

turtle.forward(length);
turtle.left(60);


### Octagon.

turtle.penup();
turtle.goto(5*length,-200);
turtle.pendown();


turtle.forward(length);
turtle.left(45);

turtle.forward(length);
turtle.left(45);

turtle.forward(length);
turtle.left(45);

turtle.forward(length);
turtle.left(45);

turtle.forward(length);
turtle.left(45);

turtle.forward(length);
turtle.left(45);


turtle.forward(length);
turtle.left(45);

turtle.forward(length);
turtle.left(45);


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


