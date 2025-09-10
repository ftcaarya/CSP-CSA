# Enter your code here
import random

number = random.randint(1, 100)

answer = int(input("Guess? "))

while number != answer:
    if number > answer:
        print("Low.")
        answer = int(input("Guess? "))
    elif number < answer:
        print("High")
        answer = int(input("Guess? "))
    else:
        print("Correct!")

