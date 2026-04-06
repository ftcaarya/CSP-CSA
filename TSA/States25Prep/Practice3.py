import math

def main(data = input("Radius or Volume? "), value = float(input("What is the value of the data: "))):
    if data == "radius":
        print(volume(value))
    else:
        print(radius(value))

def volume(radius):
    vol = (radius ** 3) * math.pi * (4/3)
    return f"{vol:.2f}"

def radius(volume):
    return f"{(((volume * 3/4) / math.pi) ** 1/3):.2f}"

main()


