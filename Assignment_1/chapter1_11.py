# -*- coding: utf-8 -*-

currentPopulation=312032486;
secondsPerBirth=7;
secondsPerDeath=13;
secondsPerImmigrant=45;


secondsPerYear=365*24*60*60;
birthsPerYear=secondsPerYear/secondsPerBirth;
deathsPerYear=secondsPerYear/secondsPerDeath;
immigrantsPerYear=secondsPerYear/secondsPerImmigrant;


changePerYear=birthsPerYear-deathsPerYear+immigrantsPerYear;
print("Population at end of First Year: ", int(currentPopulation+changePerYear));
print("Population at end of Second Year: ", int(currentPopulation+2*changePerYear));
print("Population at end of Third Year: ", int(currentPopulation+3*changePerYear));
print("Population at end of Fourth Year: ", int(currentPopulation+4*changePerYear));
print("Population at end of Fifth Year: ", int(currentPopulation+5*changePerYear));