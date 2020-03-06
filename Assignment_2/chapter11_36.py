'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


import turtle;
import random;



def travelOverMatrix(arr, row, col):

	# print("The row: ", row, " and col: ", col);
	dirs=[[1,0], [0, -1], [-1, 0], [0, 1]];
	arr[row][col]=True;
	index=random.randint(0,3);
	# print("index: ", index);
	dx=dirs[index][0];
	dy=dirs[index][1];
	if(arr[row+dx][col+dy]==True):
		# print("row: ", row+dx, "col: ",col+dy, " is visited.");
		return True;

	if(index==0):
		# print("Moving down");
		turtle.setheading(270);
		turtle.forward(30);
	elif(index==1):
		# print("Moving left");
		turtle.setheading(180);
		turtle.forward(30);
	elif(index==2):
		# print("Moving Up");
		turtle.setheading(90);
		turtle.forward(30);
	else:
		# print("Moving Right");
		turtle.setheading(0);
		turtle.forward(30);

	if(row+dx<=0 or row+dx>=16 or col+dy<=0 or col+dy>=16):
		# print("Out of boundaries.");
		return True;
	travelOverMatrix(arr, row+dx, col+dy);

	return True;



def drawBoundary():
	turtle.penup();
	#turtle.color("navy");
	turtle.forward(240);
	turtle.pendown();
	turtle.left(90);
	turtle.forward(240);
	turtle.left(90);
	turtle.forward(480);
	turtle.left(90);
	turtle.forward(480);
	turtle.left(90);
	turtle.forward(480);
	turtle.left(90);
	turtle.forward(240);
	turtle.penup();
	turtle.goto(0,0);
	turtle.pendown();



def drawGrid():
	turtle.color("skyblue");
	turtle.setheading(0);
	for j in range(-8, 9, 1):
		turtle.penup();
		turtle.goto(-240, j*30);
		# turtle.dot();
		turtle.pendown();
		turtle.forward(480);

	for i in range(-8, 9, 1):
		turtle.penup();
		turtle.goto(i*30, -240);
		turtle.pendown();
		turtle.setheading(90);
		turtle.forward(480);
	return ;






def main():


	# turtle.forward(200);
	# turtle.left(180);
	# turtle.color("white");
	# turtle.forward(200);
	# turtle.left(180);
	# turtle.color("black");


	# turtle.setheading(270);
	# turtle.forward(300);
	# turtle.penup();
	# turtle.goto(0,0);
	# turtle.pendown();

	#############################Drawing the borders for the graph.##########################

	drawBoundary();
	drawGrid();


	arr=[[False for i in range(17)] for j in range(17)];
	# print(len(arr[0]));


	turtle.penup();
	turtle.goto(0,0);
	turtle.pendown();
	turtle.color("black");
	travelOverMatrix(arr, 8, 8);


	turtle.done();


main();