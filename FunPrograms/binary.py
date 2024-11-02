def bin_to_dec(binaryNum):
    index = -1
    exp = 0
    binList = reversed(list(str(binaryNum)))
    total = 0
    
    for num in binList:
        if int(num) == 1 or int(num) == 0:
            total += int(num) * 2 ** exp
        else:
            return "Invalid Argument Passed"
            break
        exp += 1
    
    return total

def dec_to_bin(decimal):
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
        elif decimal - 2 ** exp == 0:
            decimal -= 2 ** exp
            binNum += "1"
            for i in range(exp):
                binNum += "0"
        else:
            binNum += "0"
        
        exp -= 1
        
    return int(binNum)

if input("1. bin_to_dec\n2. dec_to_bin\n") == 1:
    print(bin_to_dec(input("Enter a binary value\n")))
else:
    print(dec_to_bin(int(input("Enter a decimal value\n"))))
    
