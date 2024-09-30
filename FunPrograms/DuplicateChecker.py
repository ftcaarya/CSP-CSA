containsDuplicates = False
j = 1
myList = ['a', 'b', 'b', 'c', 'd']

while j <= (len(myList) - 1):
    k = j + 1

    while k < len(myList):
        if myList[j] == myList[k]:
            duplicate = myList[j]
            containsDuplicates = True

        k += 1
    
    j += 1

if containsDuplicates:
    print(f'duplicate found, {duplicate}')
else:
    print("No duplicates")
