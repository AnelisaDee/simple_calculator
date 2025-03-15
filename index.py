def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the seond number: "))
    operation = input("Enter the math operation (+,-, *, /): ")

    if operation == "+":
        sum = num1 + num2
        print(f"{num1} + {num2} = {sum}")
    elif operation == "-":
        sum = num1 - num2
        print(f"{num1} - {num2} = {sum}")
    elif operation == "*":
        sum = num1 * num22
        print(f"{num1} * {num2} = {sum}")
    elif operation == "/":
        if num2 != 0:
            sum = num1 / num2
            print(f"{num1} / {num2} = {sum}")
        else:
            print("Division by 0 is not allowed!")
    else:
        print("Invalid operation! Please enter one of the following: +, -, *, /.")

calculator()