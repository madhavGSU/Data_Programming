'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


import math;


def sortArray(arr):

	for i in range(len(arr)-1, 0, -1):
		for j in range(0, i):
			if(arr[j][1]>arr[j+1][1]):
				arr[j], arr[j+1]=arr[j+1], arr[j];
	return ;


def main():
	arr=[];
	str1=input("Enter student's names and scores: ").split();
	temp=[];
	for i in range(len(str1)):
		if(i%2==0):
			if(len(temp)!=0):
				arr.append(temp);
			temp=[str1[i]];
		else:
			temp.append(eval(str1[i]));
	arr.append(temp);
	sortArray(arr);

	for v in arr:
		print(v[0],v[1]);




main();