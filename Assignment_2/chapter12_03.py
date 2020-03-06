'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



from chapter7_03 import Account;




def mainMenu(account):

	option=eval(input("Main menu \n1: Check Balance\n2: Withdraw\n3: Deposit\n4: Exit"));

	while(option!=4):
		if(option==1):
			print("The balance is: ", account.getBalance());
		elif(option==2):
			amount=eval(input("Give the withdrawl amount."));
			while(amount>account.getBalance()):
				print("Withdrawl amount is greater than accout balance.");
				amount=eval(input("Give the withdrawl amount."));
			account.withdraw(amount);
		elif(option==3):
			amount=eval(input("Give the deposit money."));
			account.deposit(amount);
		option=eval(input("Main menu \n1: Check Balance\n2: Withdraw\n3: Deposit\n4: Exit"));







def main():
	# print("Yo");
	accounts=[];
	for i in range(10):
		accounts.append(Account(i, 100));

	# currentId=eval(input("Give the id from 0 to 9."));
	currentId=-1;
	while(True):
		while(currentId<0 or currentId>9):
			currentId=eval(input("Pick the id from 0 to 9."));
			
		mainMenu(accounts[currentId]);
		currentId=eval(input("Give the id from 0 to 9."));


main();




