# 4. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

n=int(input("Enter number to check whether its Armstrong or not : "))
u=n
temp=n
sum=0
count=0


while(n>0):
    count+=1
    n=n//10

while(temp>0):
    digit=temp%10
    digit=digit**count
    sum=sum+digit
    temp=temp//10

if(u==sum):
    print(f'{u} Is armstrong Number')
else:
    print(f'{u} Is not armstrong number') 