'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''



def main():
	str=input("Give the numbers between 1 and 100 separated by spaces.");
	occur=100*[0];
	strList=str.split();
	lt=[eval(x) for x in strList];


	for num in lt:
		occur[num-1]+=1;


	for i in range(0, 100):
		if(occur[i]==0):
			continue;
		if(occur[i]==1):
			print(i+1, "occurs ", occur[i], " time", sep="");
		else:
			print(i+1, "occurs ", occur[i], " times", sep="");



main();