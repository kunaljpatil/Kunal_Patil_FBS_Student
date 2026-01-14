# 5. WAP to calculate selling price of book based on cost price and discount. 
Cost = int(input("Enter The Cost price of book : "))
Discount = float(input("Enter discount that you want to give : "))

Discount_Amt = Cost*(Discount/100)
Selling_price = Cost-Discount_Amt


#Selling_Price = CostPrice - (CostPrice*(discount/100))
print(f'Selling price of book is {Selling_price}')