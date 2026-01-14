# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.

User_id = "Lokesh01"
User_pass="2005#"

i=1
while(i<=3):
    Id =input("Enter user-id: ")
    Pass =input("Enter user-password: ")

    if(User_id==Id and User_pass==Pass):
        print(f'Login successfully')
        break
    else:
        print("Invalid Credential!!!")
        if(i<3):
            print(f'Try Again You have {3-i} chance left.. \n')
        else:
             print(f'Try after 15 minutes  ')        
    i=i+1