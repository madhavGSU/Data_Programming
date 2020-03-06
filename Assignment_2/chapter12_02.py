'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



class Location():


	def __init__(self, row, column, maxValue):
		self.row=row;
		self.column=column;
		self.maxValue=maxValue;




###########################Getter Methods.##############################

	def getRow(self):
		return self.row;

	def getColumn(self):
		return self.column;

	def getmaxValue(self):
		return self.maxValue;





def locateLargest(matrix):
	if(len(matrix)==0 or len(matrix[0])==0):
		return Location(-1, -1, -1);

	maxRow=0;
	maxCol=0;
	maxValue=matrix[0][0];

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if(matrix[i][j]>maxValue):
				maxRow=i;
				maxCol=j;
				maxValue=matrix[i][j];

	return Location(maxRow, maxCol, maxValue);



def main():

	rows, cols=eval(input("Enter the number of rows, columns in the list: "));
	# matrix=[];
	# for i in range(rows):
	# 	temp=[int(x) for x in input("Enter row "+str(i)).split()];
	# 	matrix.append(temp);

	matrix=[[eval(x) for x in input("Enter row "+str(i)+": ").split()] for i in range(rows)];	
	# print(matrix);
	locationObject=locateLargest(matrix);
	print("The location of the largest object ", locationObject.getmaxValue(), " is at (", locationObject.getRow(),",", locationObject.getColumn(), ")", sep="");






main();