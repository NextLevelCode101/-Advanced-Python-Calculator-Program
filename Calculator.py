import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def exponent(x, y):
    return x ** y


def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Cannot take the square root of a negative number."


def trigonometric_functions():
    print("Choose a trigonometric function:")
    print("1. sin")
    print("2. cos")
    print("3. tan")

    choice = input("Enter choice (1/2/3): ")

    angle = float(input("Enter the angle in degrees: "))
    angle_radians = math.radians(angle)  # Convert to radians

    if choice == '1':
        return math.sin(angle_radians)
    elif choice == '2':
        return math.cos(angle_radians)
    elif choice == '3':
        return math.tan(angle_radians)
    else:
        return "Invalid input."


def calculator():
    print("Welcome to the Python Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Trigonometric Functions")
        print("8. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"The result is: {add(x, y)}")

        elif choice == '2':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"The result is: {subtract(x, y)}")

        elif choice == '3':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"The result is: {multiply(x, y)}")

        elif choice == '4':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"The result is: {divide(x, y)}")

        elif choice == '5':
            x = float(input("Enter base number: "))
            y = float(input("Enter exponent: "))
            print(f"The result is: {exponent(x, y)}")

        elif choice == '6':
            x = float(input("Enter the number: "))
            print(f"The result is: {square_root(x)}")

        elif choice == '7':
            print(trigonometric_functions())

        elif choice == '8':
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input. Please select a valid operation.")

        continue_calculating = input("Do you want to perform another operation? (yes/no): ").lower()
        if continue_calculating != "yes":
            break


if __name__ == "__main__":
    calculator()
