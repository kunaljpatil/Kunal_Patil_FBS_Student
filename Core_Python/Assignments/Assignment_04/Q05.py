# 5. WAP to print Fibonacci series upto n.
n=int(input("Print number till you want to print fibonacci series: "))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y