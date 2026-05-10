# Calculator Program 

# Imports
import time, sys

# Functions

# Ask To Contiue Function
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

# Greeting
print("Welcome to the Calculator Program!")

# Main Loop

while True: 
    # Collecting User Input and Validating the Operator
    operator = input("Enter the Operator you would like to use + - * / **: ")
    if operator not in ['+', '-', '*', '/', '**']:
        print("Invalid operator.")
        continue


# Collecting User Input and Validating the Numbers
    try:
        num1 = float(input("Enter the first number: "))

        num2 = float(input("Enter the second number: "))
        time.sleep(0.3)
    except TypeError as e1:
        time.sleep(1)
        print(f"You have error {e1}, Please Try Again")
        continue
    except ValueError as e2:
        time.sleep(1)
        print(f"You have error {e2}, Please Try Again")
        continue

# Calculating the Result

    # Addition
    if operator == "+":
        result = num1 + num2
    
    # Subtracting
    elif operator == "-":
        result = num1 - num2
    
    # Multiplying
    elif operator == "*":
        result = num1 * num2
    
    # Division
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        else:
            result = num1 / num2

    # Exponetial
    elif operator == "**":
        result = num1 ** num2
    
    # Invalid Operator
    elif operator not in ['+', '-', '*', '/', '**']:
        print("Invalid operator.")
        print("Please Try Again")
        continue


    print(f"Your answer is: {result}")
    ask_to_continue()
# Code Ends
