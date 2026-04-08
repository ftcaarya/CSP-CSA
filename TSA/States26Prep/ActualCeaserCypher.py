def actual_ceaser_cypher():
    text = input("Enter the message to be cyphered: ")
    shift = int(input("Enter the shift value: "))
    result = ""
    
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for letter in text:
        if letter.lower() in alpha:
            index = (alpha.index(letter.lower()) + shift) % 26
            if index > 25:
                index -= 26

            if letter.isupper():
                result += alpha[index].upper()
            else:
                result += alpha[index]
        else:
            result += letter
    
    return result


print(actual_ceaser_cypher())