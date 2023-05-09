operator = ""

while operator != "exit":
    # User input two numbers and an operator
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator: ")

    # Perform calculation based on operator
    if operator == "+":
        print(f"The result is: {num1 + num2}\n")
    elif operator == "-":
        print(f"The result is: {num1 - num2}\n")
    elif operator == "*":
        print(f"The result is: {num1 * num2}\n")
    elif operator == "/":
        print(f"The result is: {num1 / num2}\n")
    elif operator == "exit":
        print("Goodbye!")
    else:
        print("Invalid operator entered. Please choose from +, -, *, /, exit")