def cypher():
    message = input("Enter the message to be cyphered: ")
    shift = int(input("Enter the shift value: "))

    final = ""
    
    index = shift - 1

    for i in range(len(message)):
        if index > len(message):
            index = shift - 1 - len(message)
        final += message[index]
        index += 1
    
    print(final)

cypher()