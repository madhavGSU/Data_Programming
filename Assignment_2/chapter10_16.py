'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



def bubbleSort(lt):

	for j in range(len(lt)-1, -1, -1):
		for i in range(j):
			if(lt[i]>lt[i+1]):
				lt[i], lt[i+1]=lt[i+1], lt[i];

	return ;





def main():
	str=input("Enter 10 numbers separated by spaces.");
	# occur=100*[0];
	strList=str.split();
	lt=[eval(x) for x in strList];
	bubbleSort(lt);

	for num in lt:
		print(num, end=" ");

	print("");


main();