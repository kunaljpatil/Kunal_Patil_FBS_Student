# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random
id = "Lokesh001"
Password = "Lk123"

User_id = input("Enter your user id : ")
User_pass = input("Enter your password : ")

if(User_id==id and User_pass==Password ):
    num = random.randint(1000,9999)
    print(num)
    user_otp = int(input("Enter 4 digit code display on screen :"))
    if(num==user_otp):
        print("Login successfully")
    else:
        print("Invalid Captcha")    
elif(User_id!=id and User_pass!=Password):
    print("Invalid Credentials")
elif(User_id!=id):
    print("Invalid User-id")
else:
    print("Incorrect password")