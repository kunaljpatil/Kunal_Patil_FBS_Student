# Write a program to convert days into years, weeks and days.

# take number of days as input from user
days = int(input("Enter number of days: "))

# perform operation to find years, weeks and days
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

#display years, weeks and days
print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days,"\n")
