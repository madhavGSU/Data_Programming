'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


def sumMajorDiagonal(size):

	res=0;
	# for i in range(size):
	# 	str1=input("Enter the values of matrix row by row.");
	# 	lt=str1.split();
	# 	arr=[eval(x) for x in lt];
	# 	res+=arr[i];

	v=[];

	for i in range(size):
		str1=input("Enter the values of matrix row by row.");
		lt=str1.split();
		arr=[eval(x) for x in lt];
		v.append(arr);

	for i in range(size):
		res+=v[i][i];
	return res;



def main():
	res=0;
	size=eval(input("Size of the matrix intend to work on."));

	print("Sum of the elements in the major diagonal is: ", sumMajorDiagonal(size));








main();