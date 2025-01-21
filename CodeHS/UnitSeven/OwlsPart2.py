text = input("Enter some text: ")
splitList = text.split()
indices = []

for word in splitList:
    if word == "owls" or "owl" or "Owl" or "Owls":
        indices.append(splitList.index(word))

print(f'There were {len(indices)} words that contained "owl"')
print(f'They occured at indices: {indices}')