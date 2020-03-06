'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



def multiplyMatrix(a, b):

	#res=[[int(x) for x in input().split()] for i in range(3)];
	res=[[0]*3 for i in range(3)];

	for i in range(3):
		for k in range(3):
			for j in range(3):
				res[i][k]+=a[i][j]*b[j][k];

	return res;




def main():
	a=[];
	str1=input("Enter matrix1");
	lt=[eval(x) for x in str1.split()];
	arr=[];
	for i in range(9):
		if(i!=0 and i%3==0):
			a.append(arr);
			arr=[];
		arr.append(lt[i]);
	a.append(arr);
	#print(a);
	arr=[];

	b=[];
	str1=input("Enter matrix2");
	lt=[eval(x) for x in str1.split()];
	for i in range(9):
		if(i!=0 and i%3==0):
			b.append(arr);
			arr=[];
		arr.append(lt[i]);
	b.append(arr);
	print(b);
	res=multiplyMatrix(a, b);
	#print(res);
	for i in range(3):
		for j in range(3):
			print(round(res[i][j],2), " ", end="");
		print("");




main();	