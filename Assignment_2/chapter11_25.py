'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



def isMarkovMatrix(arr):
	cols=[0]*3;
	for i in range(3):
		for j in range(3):
			if(arr[i][j]<0):
				return False;
			cols[j]+=arr[i][j];

	for j in range(3):
		if(cols[j]!=1):
			return False;

	return True;



def main():
	print("Enter a 3X3 matrix row by row.");
	arr=[[eval(x) for x in input("").split()] for i in range(3)];
	#print(arr);
	res=isMarkovMatrix(arr);
	if(res):
		print("It is Markov Matrix.");
	else:
		print("It is not a Markov Matrix.");






main();