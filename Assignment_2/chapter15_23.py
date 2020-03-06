'''

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

'''





def displayPermutation(s):

	displayPermutationHelper("", s);






def displayPermutationHelper(s, t):
	if(t==""):
		print(s);
		return ;


	for i in range(len(t)):
		displayPermutationHelper(s+t[i], t[:i]+t[i+1:]);

	return "";	








def main():
	s=input("Give the string.");
	displayPermutation(s);





main();