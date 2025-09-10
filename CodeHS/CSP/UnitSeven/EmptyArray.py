# Enter your code here

myList = []

myList.append(3)
myList.append("hello")
myList.append(False)

for i in range(len(myList)):
    print(myList[i])

myList.remove(3)
myList.remove(False)

print(myList)