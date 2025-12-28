# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

ticket_price = int(input("Enter The Ticket Price : "))
age1=int(input("enter age 1:"))
age2=int(input("enter age 2:"))
age3=int(input("enter age 3:"))
age4=int(input("enter age 4:"))
age5=int(input("enter age 5:"))


print("**"*20)
#age1
if(age1<12):
    price1=ticket_price-ticket_price*30/100
elif(age1>59):
    price1=ticket_price-ticket_price*50/100
else:
    price1=ticket_price
print(f"{price1} as per age....")
#age2
if(age2<12):
    price2=ticket_price-ticket_price*30/100
elif(age2>59):
    price2=ticket_price-ticket_price*50/100
else:
    price2=ticket_price

print(f"{price2} as per age....")

#age3
if(age3<12):
    price3=ticket_price-ticket_price*30/100
elif(age3>59):
    price3=ticket_price-ticket_price*50/100
else:
    price3=ticket_price
 
print(f"{price3} as per age....")
    
#age4
if(age4<12):
    price4=ticket_price-ticket_price*30/100
elif(age4>59):
    price4=ticket_price-ticket_price*50/100
else:
    price4=ticket_price
    
print(f"{price4} as per age....")

#age5
if(age5<12):
    price5=ticket_price-ticket_price*30/100
elif(age5>59):
    price5=ticket_price-ticket_price*50/100
else:
    price5=ticket_price
    
print(f"{price5} as per age....")

print("**"*20)
    
total_p= price1+price2+price3+price4+price5
print(f'{total_p} is Fare price to pay tickets for all')    