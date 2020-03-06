'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''




def fillMatrix(arr,row, rows, cols, diag1, diag2):
	if(row==8):
		return True;

	for j in range(8):
		if(cols[j]==True or diag1[row-j+8]==True or diag2[row+j]==True):
			continue;
		arr[row][j]=True;
		cols[j]=True;
		diag1[row-j+8]=True;
		diag2[row+j]=True;
		if(fillMatrix(arr, row+1, rows, cols, diag1, diag2)):
			return True;
		arr[row][j]=False;
		cols[j]=False;
		diag1[row-j+8]=False;
		diag2[row+j]=False;

	return False;






def main():

	arr=[[False]*8 for i in range(8)];
	# print("size: ", len(arr[0]));
	rows=[False]*8;
	cols=[False]*8;
	diag1=[False]*17;
	diag2=[False]*17;

	fillMatrix(arr, 0, rows, cols, diag1, diag2);
	for i in range(8):
		print("|", end="");
		for j in range(8):
			if(arr[i][j]==True): 
				print("Q|",end="");
			else:
				print(" |",end="");
		print("");





main();