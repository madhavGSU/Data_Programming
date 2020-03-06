# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:18:06 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""


max1=-1;
max2=-2;


students=eval(input("Give number of students, which have to be >=2: "));

while(students<2):
    print("Number of students have to be >=2.");
    students=eval(input("Give number of students, which has to be >=2: "));

for i in range(0, students):
    score=eval(input("Give the score: "));
    if(score>=max1):
        max2=max1;
        max1=score;
    elif(score>max2):
        max2=score;
        
        
print("Highest score is: ", max1);
print("Second Highest score is: ", max2);