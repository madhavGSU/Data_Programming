'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''

import random;


def main():
	arr=[[random.randrange(2) for j in range(4)] for i in range(4)];
	print(arr);

	maxRowTotal=-1;
	maxRow=-1;
	maxColTotal=-1;
	maxCol=-1;
	cols=[0]*4;

	for i in range(4):
		rowTotal=0;
		for j in range(4):
			print(arr[i][j], "", sep=" ", end="");
			rowTotal+=arr[i][j];
			cols[j]+=arr[i][j];
		if(rowTotal>maxRowTotal):
			maxRowTotal=rowTotal;
			maxRow=i;
		print("");


	for j in range(4):
		if(cols[j]>maxColTotal):
			maxColTotal=cols[j];
			maxCol=j;

	print("The largest row index: ", maxRow);
	print("The largest column index: ", maxCol);




main();