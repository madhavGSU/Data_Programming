'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


def main():

	side1, side2, side3=eval(input("Enter the three sides of the triangle: "));
	# triObject1=Triangle();
	try:
		triObject=Triangle(side1, side2, side3);
	except TriangleError as ex:
		print("These sides: ", ex.getSide1(), ex.getSide2(), ex.getSide3(), "don't satisfy Triangle inequality theorem.")
	
	print("side1: ", triObject.getSide3());
	triObject.setColor(input("Enter the color for the triangle: "));
	triObject.setFilledState(eval(input("Enter 0 for empty or 1 for filled: ")));

	print("The area is: ", triangle.getArea());
	print("The perimeter is: ", triangle.getPerimeter());
	print("The color is: ", triangle.getColor());
	print("The Filled state is: ";, triangle.getFilledState());




class GeometricObject:
	def __init__(self, color="black", filled=True):
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
		print("color: "+self.__color+" and filled: "+str(self.__filled));




class TriangleError(RuntimeError):
	def __init__(self, side1, side2, side3):
		super().__init__();
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



class Triangle(GeometricObject):
	def __init__(self, side1=1.0, side2=1.0, side3=1.0):
		# super().__init__(color, filled);
		# if(side1+side2<=side3):
		# 	raise RuntimeError("Triangle can't be formed as these sides dont' satisfy The Triangle Inequality Theorem.")
		# if(side2+side3<=side1):
		# 	raise RuntimeError("Triangle can't be formed as these sides dont' satisfy The Triangle Inequality Theorem.")
		# if(side1+side3<=side2):
		# 	raise RuntimeError("Triangle can't be formed as these sides dont' satisfy The Triangle Inequality Theorem.")

		self.__side1=side1;
		self.__side2=side2;
		self.__side3=side3;
		GeometricObject.__init__(self);
		if not self.isValid():
			raise TriangleError(side1, side2, side3);



##########################Getter Methods.################################
	def getSide1(self):
		return self.__side1;

	def getSide2(self):
		return self.__side2;

	def getSide3(self):
		return self.__side3;



	def isValid(self):
		if(self.__side1+self.__side2<=self.__side3 or self.__side2+self.__side3<=self.__side1 or self.__side1+self.__side3<=self.__side2):
			return False;
		return True;


	def getPerimeter(self):
		return self.__side1+self.__side2+self.__side3;


	def getArea(self):
		avg=(self.__side1+self.__side2+self.__side3)/2;
		return math.sqrt(avg*(avg-self.__side1)*(avg-self.__side2)*(avg-self.__side3));


	def __str__(self):
		return "Triangle: side1="+str(self.__side1)+" side2="+str(self.__side2)+" side3="+str(self.__side3);




# def main():

# 	side1, side2, side3=eval(input("Enter the three sides of the triangle: "));
# 	# triObject1=Triangle();
# 	try:
# 		triObject=Triangle(side1, side2, side3);
# 	except TriangleError as ex:
# 		print("These sides: ", ex.getSide1(), ex.getSide2(), ex.getSide3(), "don't satisfy Triangle inequality theorem.")
	
# 	print("side1: ", triObject.getSide3());




main();