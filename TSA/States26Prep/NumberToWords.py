def number_to_words():
    number = input("Enter a number: ")

    numDict = {
        "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
        "6": "six", "7": "seven", "8": "eight", "9": "nine",
        "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
        "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen",
        "18": "eighteen", "19": "nineteen", "20": "twenty", "30": "thirty",
        "40": "forty", "50": "fifty", "60": "sixty", "70": "seventy",
        "80": "eighty", "90": "ninety",
    }

    word = ""

    if number in numDict:
        word = numDict[number]

    elif len(number) == 3:
        word += numDict[number[0]] + " hundred"
        if number[-2:] == "00":
            pass
        elif number[-2:] in numDict:
            word += " " + numDict[number[-2:]]
        else:
            if number[1] != "0":
                word += " " + numDict[number[1] + "0"]
            if number[2] != "0":
                word += " " + numDict[number[2]]

    elif len(number) == 2:
        word += numDict[number[0] + "0"]
        if number[1] != "0":
            word += " " + numDict[number[1]]

    else:
        word = numDict[number]

    print(word)

number_to_words()