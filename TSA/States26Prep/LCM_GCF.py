def lcm_gcf():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    highest = 0
    lowest = min(num1, num2)

    for i in range(1, lowest + 1):
        if num1 % i == 0 and num2 % i == 0:
            highest = i

    lcm = (num1 * num2)
    lcm = lcm // highest

    print(f"LCM: {lcm}")
    print(f"GCF: {highest}")

lcm_gcf()
