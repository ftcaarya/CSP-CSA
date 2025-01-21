numNames = int(input("Number of names: "))

names = []
for i in range(numNames):
    names.append(input("Name: "))

print(f"First name: {names[0]}")
print(f'Middle names: {names[1:(len(names) - 1)]}')
print(f'Last name: {names[len(names) - 1]}')