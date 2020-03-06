# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:53:26 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""
import random;


compNumber=random.randrange(0,3);

playerNumber=eval(input("Pick the number between Scissor(0), Rock(1), Paper(2)"));

while(playerNumber<0 or playerNumber>2):
    print("Number chosen was out of range allowed, please input once again.");
    playerNumber=eval(input("Pick the number between Scissor(0), Rock(1), Paper(2)"));


if(playerNumber==0):
    if(compNumber==0):  print("The computer is Scissor. You are Scissor. You draw.");
    elif(compNumber==1):  print("The computer is Rock. You are Scissor. You Lost.");
    elif(compNumber==2): print("The computer is Paper. You are Scissor. You won.");
elif(playerNumber==1):
    if(compNumber==0):  print("The computer is Scissor. You are Rock. You Won.");
    elif(compNumber==1):  print("The computer is Rock. You are Rock. You draw.");
    elif(compNumber==2): print("The computer is Paper. You are Rock. You Lose.");
elif(playerNumber==2):
    if(compNumber==0):  print("The computer is Scissor. You are Paper. You Lost.");
    elif(compNumber==1):  print("The computer is Rock. You are Paper. You Won.");
    elif(compNumber==2): print("The computer is Paper. You are Paper. You Draw.");