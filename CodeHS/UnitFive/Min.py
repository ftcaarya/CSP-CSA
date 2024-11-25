# Enter your code here
from jwt.utils import number_to_bytes


def minVal(numOne, numTwo):
    if numOne < numTwo:
        return numOne
    else:
        return numTwo

x = minVal(10, 14)
print(f"The min is {x}")

y = minVal(14, 16)
print(f"The min is {y}")

