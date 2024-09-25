# Enter your code here

first = int(input("First number? "))
second = int(input("Second number? "))
total = 0

for i in range(first, second + 1):
    total += i
    
print(total)