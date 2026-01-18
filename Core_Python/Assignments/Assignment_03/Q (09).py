# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1=int(input("Enter the marks of subject 1 : "))
sub2=int(input("Enter the marks of subject 2 : "))
sub3=int(input("Enter the marks of subject 3 : "))
sub4=int(input("Enter the marks of subject 4 : "))
sub5=int(input("Enter the marks of subject 5 : "))

total=sub1+sub2+sub3+sub4+sub5
percentage = (total/500)*100
percentage=round(percentage,2)

if(percentage<=100 and percentage>=80):
    print(f'First Class -->{percentage}')
elif(percentage<=79 and percentage>=60):
    print(f'Second class -->{percentage}')
elif(percentage<=59 and percentage>=30):
    print(f'third class -->{percentage}')    
else:
    print(f'Failed -->{percentage}')    

