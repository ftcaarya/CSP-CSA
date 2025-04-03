def vowels(text = input("Message: ")):
    count = 0
    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    usedVowels = ["a", "e", "i", "o", "u"]
    for let in text:
        if let in vowel:
            if let.lower() in usedVowels:
                usedVowels.remove(let.lower())

            count += 1

    print(f"Number of vowels: {count}")

    if len(usedVowels) > 0:
        print("Vowel(s) not present: " + " ".join(usedVowels))


vowels()
