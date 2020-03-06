# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 01:49:49 2020

Author: Sai Madhav Kasam.
Data Programming Assignment-1.

"""



#print(format(60.9,"<10.1f"));


empName=input("Give the employee name");
hoursWorked=eval(input("Give the number of hours worked in a week"));
hourlyRate=eval(input("Give the hourly pay rate"));
federalTax=eval(input("Give the Federal Tax Rate"));
stateTax=eval(input("Give the State Tax Rate"));
#federalTax=federalTax/100;
#stateTax=stateTax/100;
print("Employee Name:", empName);
print("Hours Worked:", format(hoursWorked, "4.1f"));
print("Pay Rate: $", hourlyRate, sep="");
grossPay=hoursWorked*hourlyRate;
print("Gross Pay: $", grossPay, sep="");
print("Deductions:");
federalHolding=federalTax*grossPay;
print("Federal Withholding (",format(federalTax*100,".2f"),"%): $",round(federalHolding,2), sep="");
stateHolding=stateTax*grossPay;
print("State Withholding (",format(stateTax*100,".2f"),"%): $",round(stateHolding, 2), sep="");
totalDeductions=stateHolding+federalHolding;
print("Total Deduction: $",totalDeductions, sep="");
netPay=grossPay-totalDeductions;
print("Net Pay: $", format(netPay, "5.2f"), sep="");