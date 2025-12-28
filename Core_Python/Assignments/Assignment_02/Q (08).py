# 8. Write a program to swap two numbers using third variable. 
num1 =int(input("Enter the number1 : "))
num2 =int(input("Enter the number2 : "))
temp = 0

print(f'\nBefore swapping')
print(f'num1 => {num1} num2 => {num2} \n')

temp = num1
num1 = num2 
num2 = temp

print(f'\nAfter swapping')
print(f'num1 => {num1} num2 => {num2}')
