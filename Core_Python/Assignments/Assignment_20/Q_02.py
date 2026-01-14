# Develop a simple calculator program that performs basic arithmetic operations (+, -, *, /) on two numbers provided by the user. The program should ask the user for the numbers and the operator. However, the program should handle the following exceptions:
    # a. Invalid Number: If the user enters a number that is not valid, catch the exception and display an error message.
    # b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or "/", catch the exception and display an error message.
    # c. Division by Zero: If the user tries to divide by zero, catch the exception and display an error message.
    # Write a program that performs the requested arithmetic operation and handles the exceptions as described above.

def add(num1, num2):
    return f'The Addition Of {num1} & {num2}: {num1 + num2}'

def sub(num1, num2):
    return f'The Subtraction Of {num1} & {num2}: {num1 - num2}'
    
def mul(num1, num2):
    return f'The Multiplication Of {num1} & {num2}: {num1 * num2}'

def div(num1, num2):
    return f'The Division Of {num1} & {num2}: {num1 / num2}'
    
try:

    x = int(input("Enter A Num1: "))
    y = int(input('Enter A Num2: '))
    op = input("Enter Operator (+, -, *, /): ")
    
    if op == '+':
        result = add(x,y)
        print(result)
    elif op == '-':
        result = sub(x,y)
        print(result)
    elif op == '*':
        result = mul(x,y)
        print(result)
    elif op == '/':
        result = div(x,y)
        print(result)
    else:
        raise ValueError("Invalid Operator!!!")
    
except ValueError as e:
    print(f'Invalid Input Error: {e}')
except ZeroDivisionError as e:
    print(e)
    
    
    
print()
print()

# Create class television that has members to hold the model number ,screen size and price. Take a member function to take input from user, If more than 4 digits are entered for model number, if screen size is smaller than 12 inches or greater than 70 inches or if the price is negative or greater than 5000 Rs, then throw an exception.
    # Write a main() that instantiates an object and allows the user to enter and display data. If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        try:
            self.model_no = int(input("Enter Model Number: "))
            self.screen_size = int(input("Enter Screen Size (inches): "))
            self.price = int(input("Enter Price: "))

            # Validation
            if len(str(self.model_no)) > 4:
                raise ValueError("Model number must be at most 4 digits")

            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen size must be between 12 and 70 inches")

            if self.price < 0 or self.price > 5000:
                raise ValueError("Price must be between 0 and 5000")

        except Exception as e:
            print("Exception occurred:", e)
            # Reset all values to zero
            self.model_no = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("Model Number:", self.model_no)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)


# main()
tv = Television()
tv.input_data()
tv.display()    
    
    
  