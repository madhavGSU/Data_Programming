'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''




def main():
	str=input("Enter the numbers separated by spaces in a line");

	lt=str.split();
	numList=[eval(x) for x in lt];
	# numList.reverse();
	i=0;
	j=len(numList)-1;
	while(i<j):
		numList[i], numList[j]=numList[j], numList[i];
		i+=1;
		j-=1;
	print(numList);



main();
