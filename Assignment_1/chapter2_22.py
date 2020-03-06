# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:38:58 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
import math;


currentPopulation=312032486;
secondsPerBirth=7;
secondsPerDeath=13;
secondsPerImmigrant=45;


secondsPerYear=365*24*60*60;
birthsPerYear=secondsPerYear/secondsPerBirth;
deathsPerYear=secondsPerYear/secondsPerDeath;
immigrantsPerYear=secondsPerYear/secondsPerImmigrant;


changePerYear=birthsPerYear-deathsPerYear+immigrantsPerYear;
yearsElapsed=eval(input("Enter the number of years: "));

#print("Population at end of First Year: ", currentPopulation+changePerYear);
#print("Population at end of Second Year: ", currentPopulation+2*changePerYear);
#print("Population at end of Third Year: ", currentPopulation+3*changePerYear);
#print("Population at end of Fourth Year: ", currentPopulation+4*changePerYear);
#print("Population at end of Fifth Year: ", currentPopulation+5*changePerYear);

print("The population in", yearsElapsed," years is: ", math.ceil(currentPopulation+yearsElapsed*changePerYear));


