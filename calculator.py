# Simple Calculator

# This function performs addition
def add(a, b):
    return a + b

# This function performs subtraction
def subtract(a, b):
    return a - b

# This function performs multiplication
def multiply(a, b):
    return a * b

# This function performs division
def divide(a, b):
    # Check if the denominator is zero to avoid errors
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


# Main program loop
while True:
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Goodbye!")
        break

    # Ask user for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform selected operation
    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))

    else:
        print("Invalid choice, please try again.")