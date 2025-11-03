def moreThanTenConv():
    index = -1
    power = 0
    global decimalNum
    decimalNum = 0
    if binaryLength >= 10:
        while -binaryLength <= index:
            if binaryNum[index] == "1":
                decimalNum = decimalNum + 1 * 2**power
                index -= 1
                power += 1
            elif binaryNum[index] == "0":
                index -= 1
                power += 1
def lessThanTenConv():
    power = 0
    global decimalNum
    decimalNum = 0
    if binaryLength <=10:
        for num in range(binaryLength):
            if binaryNum[-num-1] == "1":
                decimalNum = decimalNum + 1 * 2**power
                power += 1
            else:
                power += 1
def binary_input():
    global binaryNum
    binaryNum = input("Input a binary number: ")
    index = 0
    global binaryLength
    binaryLength = len(binaryNum)
    binaryChecked = ""
    while index <= binaryLength - 1:
        if binaryNum[index] == "0" or binaryNum[index] == "1":
            binaryChecked = binaryChecked + binaryNum[index]
            index += 1
        else:
            print("Your input", binaryNum, "is invalid.")
            binaryNum = input("Input a binary number: ")
            index = 0
            binaryLength = len(binaryNum)
    print("Your input", binaryChecked, "is valid. Good job! Let us convert it now.")
print("-"*50)
print()
print(" " * 15+ "Binary Converter V.1")
print()
print("-"*50)
print("Welcome to the Binary Converter!")
while True:
    binary_input()
    print("<Calculating>")
    if binaryLength <= 10:
        lessThanTenConv()
    else:
        moreThanTenConv()
    print("Your decimal number is " + str(decimalNum))
    choice = input("Do you want to input another binary number again (yes or no)? ")
    if choice == "yes":
        print("Great!")
        continue
    else:
        print("Thank you for using the converter!")
        break
