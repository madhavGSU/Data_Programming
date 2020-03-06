'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''


import random;



def main():

	rows=eval(input("Enter the number of rows: "));


	for i in range(rows):
		for j in range(rows):
			print(random.randint(0, 1), end=" ");
		print("");



main();	