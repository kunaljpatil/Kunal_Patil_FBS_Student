# 6. WAP to calculate total salary of employee based on basic, da=10% of basic, 
# ta=12% of basic, hra=15% of basic. 
# Basic salary (the main fixed part)
# DA (Dearness Allowance) = 10% of basic
# TA (Travel Allowance) = 12% of basic
# HRA (House Rent Allowance) = 15% of basic

Basic_Salary = int(input("Enter The Basic salary : "))
DA = Basic_Salary * (10/100)
TA = Basic_Salary * (12/100)
HRA = Basic_Salary * (15/100)
Total_Salary = int(Basic_Salary + DA + TA + HRA)

print(f'The Total Salary of employee including DA+TA+HRA+Basic is : {Total_Salary} Rs')