# def pig_latin(word):
#     vowels = "aeiouAEIOU" 
#     first_letter = word[0]
#     rest_of_word = word[1:]
#     the_special = ""

#     hasVowel = False
#     allLower = True


#     for letter in word:
#         if letter.upper() == letter:
#             allLower = False
#             break

#     for letter in word:
#         if letter in vowels:
#             hasVowel = True
#             break

#     allCaps = True

#     for i in range(len(word)):
#         if word[i].upper() != word[i]:
#             allCaps = False

#     special_characters = "!@#$%^&*()_+-=~`[]{}|;:'\",.<>?/\\"

#     for char in word:
#         if char in special_characters:
#             word = word.replace(char, "")
#             the_special += char


#     firstVowelIndex = -1;

#     for i, letter in enumerate(word):
#         if letter in vowels:
#             firstVowelIndex = i
#             break

#     new_word = ""


#     new_word = word[firstVowelIndex:] + word[:firstVowelIndex] + "ay"

#     if hasVowel == True:
#         if first_letter in vowels:
#                 new_word = word[firstVowelIndex:] + word[:firstVowelIndex] + "way"
#         else:
#                 new_word = word[firstVowelIndex:] + word[:firstVowelIndex] + "ay"
#     else:
#         new_word = word + "ay"

#     for char in new_word:
#         if char.upper() == char:
#             new_word = new_word.replace(char, char.lower())

#     pig_latin_word = new_word + the_special

#     pig_latin_word = pig_latin_word[0].upper() + pig_latin_word[1:]

#     if allCaps:
#         pig_latin_word = pig_latin_word.upper()

#     if allLower:
#         pig_latin_word = pig_latin_word.lower()

#     return pig_latin_word

# if __name__ == "__main__":
#     word = input("Enter a word to convert to Pig Latin: ")
#     print(pig_latin(word))


def pig_latin_translator(text):
    words = text.split()
    result = []
    
    for word in words:
        result.append(pig_latin_word(word))
    
    return ' '.join(result)


def pig_latin_word(word):
    VOWELS = 'aeiouAEIOU'

    isCaps = True

    for char in word:
        if char.islower():
            isCaps = False
            break
    
    punctuation = ''
    clean_word = word
    
    while clean_word and not clean_word[-1].isalpha():
        punctuation = clean_word[-1] + punctuation
        clean_word = clean_word[:-1]
    
    if not clean_word:
        return word
    
    is_capitalized = clean_word[0].isupper()
    
    lower_word = clean_word.lower()
    
    if lower_word[0] in VOWELS:
        pig_latin = lower_word + 'way'
    else:
        consonant_cluster = ''
        remaining = lower_word
        
        while remaining and remaining[0] not in VOWELS:
            if len(remaining) >= 2 and remaining[:2] == 'qu':
                consonant_cluster += 'qu'
                remaining = remaining[2:]
            else:
                consonant_cluster += remaining[0]
                remaining = remaining[1:]
        
        if not remaining:
            pig_latin = lower_word + 'ay'
        else:
            pig_latin = remaining + consonant_cluster + 'ay'
    
    if is_capitalized:
        pig_latin = pig_latin[0].upper() + pig_latin[1:]

    if isCaps:
        pig_latin = pig_latin.upper()

    
    return pig_latin + punctuation


if __name__ == "__main__":
    input_text = input()
    output = pig_latin_translator(input_text)
    print(output)