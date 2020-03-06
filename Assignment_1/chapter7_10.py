'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


import datetime;

# currTime=	datetime.datetime.now();

# print(currTime.hour);



class Time:

	def __init__(self):
		self.__hour=datetime.datetime.now().hour;
		self.__minute=datetime.datetime.now().minute;
		self.__second=datetime.datetime.now().second;




####################################Getter Methods.####################################

	def getHour(self):
		return self.__hour;



	def getMinute(self):
		return self.__minute;



	def getSecond(self):
		return self.__second;





	def setTime(self, elapsedTime):
		todaySeconds=elapsedTime%86400;
		self.__hour=todaySeconds//3600;
		todaySeconds=todaySeconds%3600;
		self.__minute=todaySeconds//60;
		todaySeconds=todaySeconds%60;
		self.__second=todaySeconds;






def main():

	obj=Time();
	print("Current hour is: ", obj.getHour());
	print("Current Minute is: ", obj.getMinute());
	print("Curent Second is: ", obj.getSecond());

	elapsedTime=eval(input("Give the elapsedTime: "));

	obj.setTime(elapsedTime);
	print("Elapsed Time's hour is: ", obj.getHour());
	print("Elapsed Time's Minute is: ", obj.getMinute());
	print("Elapsed Time's Second is: ", obj.getSecond());



main();
