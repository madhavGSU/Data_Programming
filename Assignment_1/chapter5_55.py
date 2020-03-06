'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''

import turtle;

def drawRectangle(rectCenterX, rectCenterY, width, height):

	turtle.penup();					#Botton right half.
	turtle.goto(rectCenterX, rectCenterY-height//2);
	turtle.pendown();
	turtle.forward(width//2);		# Bottom Right Half.


	turtle.left(90);				# Right side.
	turtle.forward(height);

	turtle.left(90);				# Top side.
	turtle.forward(width);

	turtle.left(90);				# Left Side.
	turtle.forward(height);

	turtle.left(90);				#Bottom Left Half.
	turtle.forward(width//2);





def main():


	width=40;

	for y in range(4, -4, -1):
		turtle.penup();
		for x in range(0,8):
			topRightX=-4*width+x*width;
			topRightY=y*width;
			rectCenterX=topRightX+(width//2);
			rectCenterY=topRightY-(width//2);
			# print("rectCenterX:", rectCenterX, " rectCenterY: ", rectCenterY);
			if((x+y)%2==1):
				turtle.begin_fill();
			drawRectangle(rectCenterX, rectCenterY, width, width);			
			if((x+y)%2==1):
				turtle.end_fill();

	turtle.done();





main();



