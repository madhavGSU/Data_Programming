'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



def main():

	rows=eval(input("Enter the number of rows in the list."));
	arr=[[eval(x) for x in input("Enter a row").split()] for i in range(rows)];

	# print(arr);

	maxVal=arr[0][0];
	maxRow=0;
	maxCol=0;

	for i in range(rows):
		for j in range(len(arr[i])):
			if(arr[i][j]>maxVal):
				maxVal=arr[i][j];
				maxRow=i;
				maxCol=j;

	res=[maxRow, maxCol];
	print("The location of the largest element is at : (",res[0], ",", res[1], ")", sep="");




main();