# 12. Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter 3digit number: "))
temp=num
Last_digit=temp%10
temp=temp//10
Middle_digit=temp%10
First_digit = temp//10
Reverse = Last_digit*100+Middle_digit*10+First_digit
if(num==Reverse):
    print("Its palindrome")
else:
    print("Its not palindrome")    