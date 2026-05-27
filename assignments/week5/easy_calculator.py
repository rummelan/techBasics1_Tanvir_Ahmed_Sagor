# Week 5 Refactoring Assignment
# Simple Calculator Program

# -------- CONSTANTS --------
WELCOME_MESSAGE = "Simple Addition Calculator"


# -------- FUNCTIONS --------
def add_numbers(num1, num2):
    """
    Adds two numbers and returns the result.
    """
    return num1 + num2


# -------- MAIN FUNCTION --------
def main():

    print(WELCOME_MESSAGE)

    # Get user input
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    # Call function
    result = add_numbers(first_number, second_number)

    # Display result
    print("The sum is:", result)


# Run the program
if __name__ == "__main__":
    main()
