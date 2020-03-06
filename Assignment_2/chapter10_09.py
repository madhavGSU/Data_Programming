'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


import math;



def mean(lt):
	total=0;
	for num in lt:
		total+=num;

	avg=total/len(lt);
	print("The mean is: ", round(avg, 2));
	return avg;


def deviation(lt):
	avg=mean(lt);
	total=0;
	size=len(lt);
	for num in lt:
		total+=math.pow(num-avg, 2);
	total/=(size-1);
	deviation=math.sqrt(total);
	print("The standard deviation is:", round(deviation, 5));
	return deviation;




def main():
	str=input("Give the numbers between 1 and 100 separated by spaces: ");
	# occur=100*[0];
	strList=str.split();
	lt=[eval(x) for x in strList];
	# print(lt)
	deviation(lt);






main();