names = []
temp = []
for i in range(5):
    name = input("Name: ")
    temp = name.split()
    names.append(temp[-1])
    temp.clear()

print(sorted(names))