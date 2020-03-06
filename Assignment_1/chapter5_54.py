'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''



import turtle;


def main():


	turtle.penup();
	turtle.goto(-100,0);
	turtle.pendown();
	turtle.forward(200);
	turtle.stamp();
	turtle.penup();
	turtle.goto(0, -300);
	turtle.setheading(90);
	turtle.pendown();
	turtle.forward(600);
	turtle.penup();
	turtle.goto(-20,400);
	turtle.pendown();

	for x in range(-80, 81):
		turtle.goto(x*0.25, (x*0.25)**2);




	turtle.done();







main();