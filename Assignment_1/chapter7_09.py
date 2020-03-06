'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


class LinearEquation:

	def __init__(self, a, b, c, d, e, f):
		self.__a=a;
		self.__b=b;
		self.__c=c;
		self.__d=d;
		self.__e=e;
		self.__f=f;



#################################Setter Methods.###############################

	def setA(self,value):
		self.__a=value;

	def setB(self,value):
		self.__b=value;

	def setC(self,value):
		self.__c=value;

	def setD(self,value):
		self.__d=value;

	def setE(self,value):
		self.__e=value;

	def setF(self,value):
		self.__f=value;







################################Getter Methods.##################################


	def getA(self):
		return self.__a;

	def getB(self):
		return self.__b;

	def getC(self):
		return self.__c;

	def getD(self):
		return self.__d;

	def getE(self):
		return self.__e;

	def getF(self):
		return self.__f;




################################Other Methods.#####################################


	def isSolvable(self):
		value=(self.__a*self.__d)-(self.__b*self.__c);
		if(value==0):
			return False;
		else: 
			return True;


	def getX(self):
		numer=(self.__e*self.__d)-(self.__b*self.__f);
		denom=(self.__a*self.__d)-(self.__b*self.__c);
		return numer/denom;


	def getY(self):
		numer=(self.__a*self.__f)-(self.__e*self.__c);
		denom=(self.__a*self.__d)-(self.__b*self.__c);
		return numer/denom;




def main():
	x1=eval(input("Give the number for x1: "));
	y1=eval(input("Give the number for y1: "));
	x2=eval(input("Give the number for x2: "));
	y2=eval(input("Give the number for y2: "));
	x3=eval(input("Give the number for x3: "));
	y3=eval(input("Give the number for y3: "));
	x4=eval(input("Give the number for x4: "));
	y4=eval(input("Give the number for y4: "));

	slope1=(y2-y1)/(x2-x1);
	slope2=(y4-y3)/(x4-x3);


	####################First Line Equation.##########################
	a=-slope1;
	b=1;
	e=y2-(slope1*x2);


	####################Second Line Question.##########################
	c=-slope2;
	d=1;
	f=y4-(slope2*x4);




	eqn=LinearEquation(a, b, c, d, e, f);
	if(eqn.isSolvable()==False):
		print("The Equation has no solution.");
	else:
		print("The x coordiante of intersecting point is: ", eqn.getX());
		print("The y coordiante of intersecting point is: ", eqn.getY());



main();