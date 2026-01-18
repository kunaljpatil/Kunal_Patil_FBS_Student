# 12. WAP to print Armstrong number within a given range
n1=int(input("Enter starting range:"))
n2=int(input("Enter ending range:"))
for i in range(n1,n2+1):

    sum=0
    temp=i
    count=0
    num=i

    while(num>0):
        count+=1
        num=num//10

    while(temp>0):
        digit=temp%10
        digit=digit**count
        sum=sum+digit
        temp=temp//10    

    if(i==sum):
        print(f'{i} is Armstrong')

