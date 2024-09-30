# Enter your code here

MAX = 1000

def fibonacci_sequence():
    a, b = 1, 1
    while a <= MAX:
        print(a)
        a, b = b, a + b

fibonacci_sequence()