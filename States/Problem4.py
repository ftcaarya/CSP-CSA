def fizz_buzz(nums = int(input("Enter a number: "))):
    print("Fizz...Buzz...FizzBuzz")
    s = ""

    for num in range(1, nums + 1):
        if num % 3 == 0 and num % 5 != 0:
            s += " Fizz"
        elif num % 5 == 0 and num % 3 != 0:
            s += " Buzz"
        elif num % 3 == 0 and num % 5 == 0:
            s += " FizzBuzz"
        else:
            s += f" {num}"

    print(s[1:])

fizz_buzz()