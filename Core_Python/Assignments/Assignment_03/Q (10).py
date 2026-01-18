# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
mage=int(input("Enter Male Age:"))
fage=int(input("Enter Female Age:"))

if(mage>=21 and fage >=18):
    print("Eligible for marry")
elif(mage >= 21):
    print("Mage valid for marry f not")
elif(fage>=18):
    print("fage is valid but m not")
else:
    print("Not Allow to Marry")