# 9. Write a program to swap two numbers without using third variable. 
num1=int(input("Enter The num1: "))
num2=int(input("Enter The num2: "))

print(f'\nBefore swap')
print(f'num1={num1} \n num2={num2}\n')

num1,num2 = num2,num1   # num1,num2 = (value2,value1) rhs convert in tuple and value assigned

print(f'\nAfter swap')
print(f'num1={num1} \n num2={num2}\n')