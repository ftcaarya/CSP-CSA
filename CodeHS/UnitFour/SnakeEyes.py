# Enter your code here

import random

counter = 0

while True:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    
    counter += 1
    print(f"Rolled: {num1} {num2}")
    if num1 == 1 and num2 == 1:
        print(f"It took you {counter} rolls to get snake eyes.")
        break