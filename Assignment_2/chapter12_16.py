'''

Author: Sai Madhav Kasam
Data Programming Assignment-1.


'''


class Stack(list):

	def __init__(self):
		pass;


	def top(self):
		return self[len(self)-1];



	def push(self, val):
		self.append(val);



	##########################Since list's pop behavior is same as what we want for Stack, we just inherit.#########################		
	# def pop(self):
	# 	self.pop();
	# 	return ;



	def size(self):
		return len(self);


	def isEmpty(self):
		return (len(self)==0);



def main():

	####################Below code tests all functionalities of the Stack.######################
	# st=Stack();
	# if(st.empty()):
	# 	print("Stack is empty.");
	# st.push(10);
	# print(st.top());
	# st.push(20);
	# print(st.size());
	# st.pop();
	# print(st.top());
	# if(st.empty()):
	# 	print("Stack is empty");
	# else:
	# 	print("Stack is not empty.");


	st=Stack();
	for i in range(5):
		str1=input("Give the string.");
		st.push(str1);

	while(not st.isEmpty()):
		print(st.top());
		st.pop();


main();