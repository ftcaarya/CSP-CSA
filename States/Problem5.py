import string

def remove_punctuation(sentence):
    clean_sentence = ""
    for char in sentence:
        if char not in string.punctuation:
            clean_sentence += char
    return clean_sentence.split()

def word_count(sentence):
    words = remove_punctuation(sentence)
    count = {}
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count

def count_vowels(sentence):
    vowels = "AEIOUaeiou"
    total = 0
    for char in sentence:
        if char in vowels:
            total += 1
    return total

def common_word_frequencies(s1 = input("Enter the first sentence: "), s2 = input("Enter the second sentence: ")):
    count1 = word_count(s1)
    count2 = word_count(s2)

    common = []
    for word in count1:
        if word in count2:
            total = count1[word] + count2[word]
            common.append(word + " - " + str(total))

    unique = []
    for word in count1:
        if word not in count2:
            unique.append(word)
    for word in count2:
        if word not in count1 and word not in unique:
            unique.append(word)

    if len(common) > 0:
        print("Words in both sentences: " + ", ".join(common))

    if len(unique) > 0:
        print("Unique words: " + ", ".join(unique))

    total_vowels = count_vowels(s1) + count_vowels(s2)
    print("Number of vowels:", total_vowels)


common_word_frequencies()
