# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:38:14 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""

import random;


number=random.randrange(0,52);

# number=eval(input("Give a number between 0 and 51"));


rank=["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
suit=["Clubs", "Diamonds", "Hearts", "Spades"];

rankIndex=number%13;
suitIndex=number//13;

print("The card you picked is the", rank[rankIndex], "of", suit[suitIndex]);