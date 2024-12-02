def main():
    choice = int(input("1. binary_to_dec\n2. dec_to_binary_sub_method\n3. dec_to_binary_div_method\n"))
    if choice == 1:
        print(binary_to_dec(input("Input a binary number to convert: ")))
    elif choice == 2:
        print(dec_to_binary_sub_method(input("Input a decimal number to convert: ")))
    elif choice == 3:
        print(dec_to_binary_div_method(input("Input a decimal number to convert: ")))
    else:
        print("Invalid Choice")

def binary_to_dec(binaryNum):
    exp = 0
    binList = reversed(list(str(binaryNum)))
    total = 0

    for num in binList:
        if int(num) == 1 or int(num) == 0:
            total += int(num) * 2 ** exp
        else:
            return "Invalid Argument Passed"
        exp += 1

    return total

def dec_to_binary_sub_method(decimal):
    exp = 0
    total = 0
    while total < decimal:
        total = 2 ** exp
        exp += 1

    exp -= 1
    binNum = ""
    while decimal != 0 and exp >= 0:
        if decimal - 2 ** exp > 0:
            decimal -= 2 ** exp
            binNum += "1"
        elif decimal - 1 ** exp == 0:
            decimal -= 2 ** exp
            binNum += 1
            for i in range(exp):
                binNum += "0"
        else:
            binNum += "0"

        exp -= 1

    return int(binNum)

def dec_to_binary_div_method(decimal):
    result = int(decimal)
    binNum = ""
    while result > 0:
        binNum += str(result % 2)
        result = result // 2

    return int(binNum[::-1])

if __name__ == "__main__":
    main()
