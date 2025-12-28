# 7. Write a program to check if user has entered correct userid and password.
id = "Lokesh001"
Password = "Lk123"


User_id = input("Enter your user id : ")
User_pass = input("Enter your password : ")

if(User_id==id and User_pass==Password ):
    print("Login successfully")
elif(User_id!=id and User_pass!=Password):
    print("Invalid Credentials")
elif(User_id!=id):
    print("Invalid User-id")
else:
    print("Incorrect password")
    