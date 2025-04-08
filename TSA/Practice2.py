def replace(orig = input("Enter original string: "), to_replace = input("What word would you want to replace: "), replace_with = input("What would you want to replace with: ")):
    split_orig = orig.split()
    for i, word in enumerate(split_orig):
        if word == to_replace:
            split_orig.remove(word)
            split_orig.insert(i, replace_with)

    print(" ".join(split_orig))

replace()