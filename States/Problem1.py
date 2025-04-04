from pydantic import validate_email


def temp():
    print("In order to convert the provided temperature please input the temperature and first initial of the scale. (F - Fahrenheit, C - Celsius, K - Kelvin)")
    init = input("Please enter temperature and scale: ")
    print("Conversion Options: \n    1.  Convert to Celsius\n    2.  Convert to Fahrenheit\n    3.  Convert to Kelvin")
    convert = int(input("Please select the scale you wish to convert your temperature to: "))

    same = False
    typeD = init[-1]
    value = int(init[:len(init) - 1])
    actual = ""
    # print(value)
    result = 0.0
    # :.2f
    if typeD == "C" and convert == 3:
        result = value + 273.15
        actual = "Kelvin"
    elif typeD == "K" and convert == 1:
        result = value - 273.15
        actual = "Celsius"
    elif typeD == "F" and convert == 1:
        result = (value - 32) * (5/9)
        actual = "Celsius"
    elif typeD == "C" and convert == 2:
        result = value * (9/5) + 32
        actual = "Fahrenheit"
    elif typeD == "F" and convert == 3:
        result = (value - 32) * (5/9) + 273.15
        actual = "Kelvin"
    elif typeD == "K" and convert == 2:
        result = (value - 273.15) * (9/5) + 32
        actual = "Fahrenheit"
    elif (typeD == "F" and convert == 2) or (typeD == "C" and convert == 1) or (typeD == "K" and convert == 3):
        same = True

    if same == True:
        print("Temperature is already in the desired scale")
    else:
        print(f"Converted Temperature: {result:.2f} {actual}")

temp()