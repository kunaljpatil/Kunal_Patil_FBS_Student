# 11. Write a program to accept an integer amount from user and tell minimum 
# number of notes needed for representing that amount. 
amt = int(input("Enter the Amount:"))

temp = amt

n2000 = temp//2000 
print(f'{n2000} notes of 2000')
temp = temp % 2000 

n500 = temp//500 
print(f'{n500} notes of 500')
temp = temp % 500 

n200 = temp//200 
print(f'{n200} notes of 200')
temp = temp % 200 

n100 = temp//100 
print(f'{n100} notes of 100')
temp = temp % 100 

n50 = temp//50 
print(f'{n50} notes of 50')
temp = temp % 50 

n20 = temp//20 
print(f'{n20} notes of 20')
temp = temp % 20 

n10 = temp//10 
print(f'{n10} notes of 10')
temp = temp % 10 

c5 = temp//5 
print(f'{c5} coins of 5')
temp= temp % 5

c2 = temp // 2
print(f'{c2} coins of 2')
temp = temp%2

c1 = temp // 1
print(f'{c1} coins of 1')
print("******************************************************************")

total_n = n2000+n500+n200+n100+n50+n20+n10
print(f"{total_n}Minimum Notes Required for this Amount" )

coins_n = c5+c2+c1
print(f'{coins_n} Coins Required for this remaining amount')