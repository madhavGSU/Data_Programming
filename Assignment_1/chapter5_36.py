# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:53:26 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""
import random;


#compNumber=random.randrange(0,3);

#playerNumber=eval(input("Pick the number between 0, 1, 2"));



'''
while(playerNumber<0 or playerNumber>2):
    print("Number chosen was out of range allowed, please input once again.");
    playerNumber=eval(input("Pick the number between 0, 1, 2"));
'''


computer=0;
player=0;
while(True):
    
    compNumber=random.randrange(0,3);
    playerNumber=eval(input("Pick the number between 0, 1, 2: "));
    if(playerNumber==0):
        if(compNumber==0):  
            print("The computer is Scissor. You are Scissor. You draw.");
        elif(compNumber==1):  
            print("The computer is Rock. You are Scissor. You Lost.");
            computer+=1;
        elif(compNumber==2): 
            print("The computer is Paper. You are Scissor. You won.");
            player+=1;
    elif(playerNumber==1):
        if(compNumber==0):  
            print("The computer is Scissor. You are Rock. You Won.");
            player+=1;
        elif(compNumber==1):  
            print("The computer is Rock. You are Rock. You draw.");
        elif(compNumber==2): 
            print("The computer is Paper. You are Rock. You Lose.");
            computer+=1;
    elif(playerNumber==2):
        if(compNumber==0):  
            print("The computer is Scissor. You are Paper. You Lost.");
            computer+=1;
        elif(compNumber==1):  
            print("The computer is Rock. You are Paper. You Won.");
            player+=1;
        elif(compNumber==2): 
            print("The computer is Paper. You are Paper. You Draw.");

    if(player>2 or computer>2):
        break;




