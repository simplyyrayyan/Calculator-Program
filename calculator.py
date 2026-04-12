# Calculator Program 

import time
import sys 

print("Welcome to the Calculator Program!")

# Ask To Contiue Functions
def ask_to_continue():
    user_input1 = input("Would you like to (Quit) or (Continue)?: ").lower().strip()
    if user_input1 == "quit":
        time.sleep(0.8)
        print("Thanks for using the Calculator Program hope to see you again!")
        sys.exit()
    elif user_input1 == "continue":
        time.sleep(0.8)
        return True
    else:
        print("Invalid Number")
        return True 

while True: 
    # Collecting User Input and Validating the Operator
    operator = input("Enter the Operator you would like to use + - * / **: ")
    if operator not in ['+', '-', '*', '/', '**']:
        print("Invalid operator. Please enter one of the following: +, -, *, /, **.")
        continue


# Collecting User Input and Validating the Numbers
    try:
        num1 = float(input("Enter the first number: "))

        num2 = float(input("Enter the second number: "))
        time.sleep(0.3)
    except ValueError:
        time.sleep(1)
        print("Invalid input. Please enter a valid number.")
        continue

    # Calculating the Result

    # Addition
    if operator == "+":
        result = num1 + num2
        print(f"Your answer is: {result}")
        ask_to_continue()
    
    # Subtracting
    elif operator == "-":
        result = num1 - num2
        print(f"Your answer is: {result}")
        ask_to_continue()
    
    # Multiplying
    elif operator == "*":
        result = num1 * num2
        print(f"Your answer is: {result}")
        ask_to_continue()
    
    # Division
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Your answer is: {result}")

        ask_to_continue()

    # Exponetial
    elif operator == "**":
        result = num1 ** num2
        print(f"Your answer is: {result}")
        ask_to_continue()

# Code Ends
