# 10. Write a program to reverse three-digit number. 
num =int(input("Enter Three digit Number : "))
Temp = num # ex 345
d1 = Temp % 10 #last digit stored --> 5
Temp = Temp // 10 # num become 2digit --> 34
d2 = Temp % 10 # get last digit --> 4
d3 = Temp // 10 # get first digit -->3

print(f'Num before reverse : {num}')
print(f'\n Num After reverse : {d1}{d2}{d3}')