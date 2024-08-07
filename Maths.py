def calculate():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nAvailable Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    operation = int(input("\nEnter the operation number: "))

    if operation == 1:
        print("Result:", num1 + num2)
    elif operation == 2:
        print("Result:", num1 - num2)
    elif operation == 3:
        print("Result:", num1 * num2)
    elif operation == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed")
    elif operation == 5:
        print("Exiting the calculator...")
    else:
        print("Error: Invalid operation number")

while True:
    calculate()