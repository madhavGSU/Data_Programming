'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


import turtle;
import random;
import math;


# rectCenterX=-75;
# rectCenterY=0;
# width=100;
# height=100;


def drawRectangle(rectCenterX, rectCenterY, width, height):

	turtle.penup();					#Botton right half.
	turtle.goto(rectCenterX, rectCenterY-height//2);
	turtle.pendown();
	turtle.forward(width//2);


	turtle.left(90);				# Right side.
	turtle.forward(height);

	turtle.left(90);				# Top side.
	turtle.forward(width);

	turtle.left(90);				# Left Side.
	turtle.forward(height);

	turtle.left(90);				#Bottom Left Half.
	turtle.forward(width//2);



# circleCenterX=50;
# circleCenterY=0;
# radius=50;

def drawCircle(circleCenterX, circleCenterY, radius):
	turtle.penup();
	turtle.goto(circleCenterX, circleCenterY-radius);
	turtle.pendown();
	turtle.circle(radius);









def main():

	##########################Rectangle Measurements.##############
	rectCenterX=-75;
	rectCenterY=0;
	width=100;
	height=100;
	drawRectangle(rectCenterX, rectCenterY, width, height);



	###############################Circle Measurements.###############
	circleCenterX=50;
	circleCenterY=0;
	radius=50;
	drawCircle(circleCenterX, circleCenterY, radius);


	rectBottomLeftX=rectCenterX-(width//2);
	rectBottomLeftY=rectCenterY-(height//2);



	for i in range(10):
		randX=random.random();
		randY=random.random();
		#print("x: ", randX);
		turtle.penup();
		turtle.goto(rectBottomLeftX+(randX*width), rectBottomLeftY+(randY*height));
		turtle.pendown();
		turtle.dot();



	#print(10*math.cos(math.radians(180)));
	for i in range(10):
		fraction=random.uniform(0,1);
		tempRadius=radius*fraction;
		degrees=random.randint(-180, 180);

		turtle.penup();
		turtle.goto(circleCenterX+(tempRadius*math.cos(math.radians(degrees))), circleCenterY+(tempRadius*math.sin(math.radians(degrees))));
		turtle.pendown();
		turtle.dot();



	turtle.done();


main();