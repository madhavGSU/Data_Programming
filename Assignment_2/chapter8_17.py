import math;


class Point():

	def __init__(self, x=0, y=0):
		self.__x=x;
		self.__y=y;





##################Getter Methods.######################


	def getX(self):
		return self.__x;

	def getY(self):
		return self.__y;




	def distance(self, other):
		total=math.pow(abs(self.__x-other.getX()), 2)+math.pow(abs(self.__y-other.getY()), 2);
		dist=math.sqrt(total);
		#print("Total dist: ", dist);
		return dist;


	def isNearBy(self, other):
		dist=self.distance(other);
		if(dist<=5):
			return True;
		else:
			return False;


	def __str__(self):
		res="("+str(self.__x)+","+str(self.__y)+")";
		return res;





def main():
	x1=eval(input("Give the x coordinate of the first point."));
	y1=eval(input("Give the y coordinate of the first point."));

	x2=eval(input("Give the x coordinate of the second point."));
	y2=eval(input("Give the y coordinate of the second point."));
	p=Point(x1, y1);
	q=Point(x2, y2);
	#print("x: ", p.getX());

	print("The distance between two points is: ", round(p.distance(q), 2));

	if(p.isNearBy(q)):
		print("The two points are near to each other.");
	else:
		print("The two points are not near to each other.");

	##############################################Tests the __str__ overriding function.###################################
	#print("The string form is: ", str(p));




main();