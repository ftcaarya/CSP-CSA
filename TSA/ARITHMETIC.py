def arithmetic(num1 = int(input("1st Number: ")), num2 = int(input("2nd Number: ")), oper = input("Operater: ")):
    if oper == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif oper == "/":
        if num2 == 0:
            print("Error: Division by Zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    elif oper == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif oper == "-":
        print(f"{num1} - {num2} = {num1 - num2}")

arithmetic()