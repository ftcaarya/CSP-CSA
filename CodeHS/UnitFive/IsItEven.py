SENTINEL = 0

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

answer = int(input("Enter a number: "))

while answer != SENTINEL:
    if is_even(answer):
        print("Even")
    else:
        print("Odd")

    answer = int(input("Enter a number: "))

    if answer == SENTINEL:
        print("Done!")
        break