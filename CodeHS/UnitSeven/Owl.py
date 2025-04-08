def owl_count(text):
    counter = 0
    textSplit = text.split()
    for word in textSplit:
        for j, letter in enumerate(word):
            if letter == "o" or letter =="O":
                if j + 3 <= len(word):
                    if word[j + 1] == "w" and word[j + 2] == "l":
                        counter += 1

    return counter