'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


import math;


class RegularPolygon:

	def __init__(self, n=3, side=1, x=0, y=0):
		self.__n=n;
		self.__side=side;
		self.__x=x;
		self.__y=y;



	#################################Getter Methods.##################################

	def getN(self):
		return self.__n;

	def getSide(self):
		return self.__side;

	def getX(self):
		return self.__x;

	def getY(self):
		return self.__y;



	#################################Setter Methods.#################################



	def setN(self, value):
		self.__n=value;

	def setSide(self, value):
		self.__side=value;

	def setX(self, value):
		self.__x=value;

	def setY(self, value):
		self.__y=value;


	##################################Other Methods.#####################################


	def getPerimeter(self):
		return (self.__n*self.__side);

	def getArea(self):
		numer=self.__n*self.__side*self.__side;
		denom=4*math.tan(math.radians(180/self.__n));
		return numer/denom;



def main():
	obj1=RegularPolygon();
	obj2=RegularPolygon(6, 4);
	obj3=RegularPolygon(10, 4, 5.6, 7.8);


	print("First object Perimeter: ", obj1.getPerimeter());
	print("First object Area is: ", obj1.getArea());


	print("Second object Perimeter is: ", obj2.getPerimeter());
	print("Second object Area is: ", obj2.getArea());


	print("Third object Perimater is: ", obj3.getPerimeter());
	print("Third object Area is: ", obj3.getArea());



main();