'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


class Account:
	def __init__(self, id=0, initBlance=100.0, interestRate=0.0):
		self.__id=id;
		self.__balance=initBlance;
		self.__interestRate=interestRate;



	##############################Getter Methods.##########################
	def getId(self):
		return self.__id;

	def getBalance(self):
		return self.__balance;

	def getinterestRate(self):
		return self.__interestRate;


	##############################Setter Methods.##########################
	def setId(self, value):
		self.__id=value;

	def setBalance(self, value):
		self.__balance=value;	

	def setinterestRate(self, value):
		self.__interestRate=value;


	################################Other Methods.###########################


	def getMonthlyInterestRate(self):
		return self.__interestRate/12;

	def withdraw(self, value):
		self.__balance-=value;


	def deposit(self, value):
		self.__balance+=value;


	def getMonthlyInterest(self):
		return self.__balance*self.getMonthlyInterestRate()*0.01;



def main():

	acct=Account(1122,20000, 4.5);
	acct.withdraw(2500);
	acct.deposit(3000);
	print("id is: ", acct.getId());
	print("balance is: ", acct.getBalance(), "$", sep="");
	print("Monthly interest Rate is: ", acct.getMonthlyInterestRate());
	print("Monthly interest is: ", acct.getMonthlyInterest(), "$", sep="");




main();