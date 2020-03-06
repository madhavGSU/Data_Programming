'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''




def main():
	str1=input("Enter the first sorted list1.");
	lt=str1.split();
	nums1=[eval(x) for x in lt];


	str2=input("Enter the Second sorted list");
	lt2=str2.split();
	nums2=[eval(x) for x in lt2];

	i=0;
	j=0;

	res=[];
	while(i<len(nums1) or j<len(nums2)):
		if(i<len(nums1) and j<len(nums2)):
			if(nums1[i]<=nums2[j]):
				res.append(nums1[i]);
				i+=1;
			else:
				res.append(nums2[j]);
				j+=1;
		elif(i<len(nums1)):
			res.append(nums1[i]);
			i+=1;
		else:
			res.append(nums2[j]);
			j+=1;

	print("The merged list is: ", end="");

	for num in res:
		print(num,"", end="");
	print("");




main();