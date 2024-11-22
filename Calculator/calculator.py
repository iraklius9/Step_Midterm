def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()

        if operation == '+':
            return f"Result: {num1 + num2}"
        elif operation == '-':
            return f"Result: {num1 - num2}"
        elif operation == '*':
            return f"Result: {num1 * num2}"
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return f"Result: {num1 / num2}"
        else:
            return "Error: Invalid operation. Please choose from +, -, *, or /."
    except ValueError:
        return "Error: Invalid input. Please enter valid numbers."


while True:
    print(calculator())
    if input("Do you want to calculate again? (yes/no): ").strip().lower() != 'yes':
        break


