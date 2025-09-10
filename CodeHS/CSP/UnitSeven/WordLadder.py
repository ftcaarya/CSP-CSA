def enter_word():
    return input("Enter a word: ")


def get_index(word):
    while True:
        try:
            index = int(input("Enter a index (-1 to quit): "))
            if index < -1 or index >= len(word):
                print("invalid index")
            else:
                return index

        except ValueError:
            print("invalid index")

def get_letter():
    letter = input("Enter a letter: ")
    while letter == letter.upper() or len(letter) != 1:
        if letter == letter.upper():
            print("Character must be a lowercase letter!")
        if len(letter) != 1:
            print("Must be exactly one character!")
        letter = input("Enter a letter: ")

    return letter

def new_word(word, index, letter):
    return word[0:index] + letter + word[index + 1:]

word = enter_word()

while True:
    index = get_index(word)
    if index == -1:
        break

    word = new_word(word, index, get_letter())
    print(word)