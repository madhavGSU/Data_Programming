'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


import math;






class GeometricObject():
	def __init__(self, color, filled):
		self.__color=color;
		self.__filled=filled;



#####################################Getter Methods.####################################

	def getColor(self):
		return self.__color;

	def getFilledState(self):
		return self.__filled;


#####################################Setter Methods.###################################

	def setColor(self, color):
		self.__color=color;	

	def setFilledState(self, filled):
		self.__filled=filled;


	def __str__(self):
		print("This is geometric object.");




class Triangle(GeometricObject):
	def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="black", filled="False"):
		super().__init__(color, filled);
		self.__side1=side1;
		self.__side2=side2;
		self.__side3=side3;




##########################Getter Methods.################################
	def getSide1(self):
		return self.__side1;

	def getSide2(self):
		return self.__side2;

	def getSide3(self):
		return self.__side3;




	def getPerimeter(self):
		return self.__side1+self.__side2+self.__side3;


	def getArea(self):
		avg=(self.__side1+self.__side2+self.__side3)/2;
		return math.sqrt(avg*(avg-self.__side1)*(avg-self.__side2)*(avg-self.__side3));


	def __str__(self):
		return "Triangle: side1="+str(self.__side1)+" side2="+str(self.__side2)+" side3="+str(self.__side3);


def main():

	side1, side2, side3=eval(input("Give three sides of the triangle separted by commas: "));
	color=input("Give the color for the triangle.");
	filled=bool(input("Enter 1 for filled or 0 for unfilled."));
	tri1=Triangle(side1, side2, side3, color, filled);
	print("Area is:", tri1.getArea());
	print("Perimeter is: ", tri1.getPerimeter());
	print("The color of triangle is: ", tri1.getColor())
	print("Filled state is: ", tri1.getFilledState());
	print(str(tri1));






main();
