'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


def isSorted(lt):

	if(len(lt)<=1):
		return True;

	prev=lt[0];

	for i in range(1, len(lt)):
		if(prev>lt[i]):
			return False;
		prev=lt[i];
	return True;





def main():

	str=input("Give the numbers between 1 and 100 separated by spaces.");
	strList=str.split();
	lt=[eval(x) for x in strList];

	if(isSorted(lt)):
		print("The list is already sorted.");
	else:
		print("The list is not sorted.");







main();