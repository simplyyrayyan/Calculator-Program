# Calculator Program 

# Imports
import sys
from slow_printing import slow_print, slow_input

operator = ['+', '-', '*', '/', '**']
# Functions

# Ask To Contiue Function
def ask_to_continue():
    user_countiue = slow_input("Would you like to (Quit) or (Continue)?: ").lower().strip()
    if user_countiue == "quit":
        slow_print("Thanks for using the Calculator Program hope to see you again!")
        sys.exit()
    elif user_countiue == "continue":
        return True
    else:
        slow_print("Invalid Number")
        return True

# Greeting
slow_print("Welcome to the Calculator Program!")

# Main Loop
def main():
    while True: 
        # Collecting User Input and Validating the Operator
        operators = slow_input("Enter the Operator you would like to use (*operator): ")
        if operators not in operator:
            slow_print("Invalid operator.")
            continue


    # Collecting User Input and Validating the Numbers
        try:
            num1 = float(slow_input("Enter the first number: "))
            num2 = float(slow_input("Enter the second number: "))
        except TypeError:
            slow_print(f"You have a TypeError, Please Try Again")
            continue
        except ValueError:
            slow_print(f"You have a ValueError, Please Try Again")
            continue

    # Calculating the Result

        # Addition
        if operators == "+":
            result = num1 + num2

        # Subtracting
        elif operators == "-":
            result = num1 - num2

        # Multiplying
        elif operators == "*":
            result = num1 * num2
    
        # Division
        elif operators == "/":
            if num2 == 0:
                slow_print("Error: Division by zero is not allowed.")
                continue
            else:
                result = num1 / num2

        # Exponetial
        elif operators == "**":
            result = num1 ** num2
    
        # Invalid Operator
        elif operators not in ['+', '-', '*', '/', '**']:
            slow_print("Invalid operator.")
            slow_print("Please Try Again")
            continue


        print(f"Your answer is: {result}")
        ask_to_continue()
    # Code Ends

if __name__ == "__main__":
    main()
