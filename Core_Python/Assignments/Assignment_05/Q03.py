# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

Num_passenger =int(input("Enter the number of passenger: "))
Ticket_cost=int(input("Enter ticket cost: "))
Total_amount=0

for i in range(1,Num_passenger+1):

    Age=int(input(f"\nEnter age of {i} passenger:"))

    if(Age<12):
        Ticket=Ticket_cost-Ticket_cost*0.30
        print(f"Passenger {i} of age {Age} have to pay :{Ticket} Rs\n")
    elif(Age>59):
        Ticket=Ticket_cost-Ticket_cost*0.50
        print(f"Passenger {i} of age {Age} have to pay :{Ticket} Rs") 
    else:
        Ticket=Ticket_cost
        print(f"Passenger {i} of age {Age} have to pay :{Ticket} Rs") 

    Total_amount+=Ticket    

print(f'\n Total ticket amount for {i} passengers is :{Total_amount} Rs\n')              