# Enter your code here

N = int(input("Enter a non-negative integer N to calculate N!: "))

factorial_result = 1

for i in range(1, N + 1):
    factorial_result *= i

print(factorial_result)