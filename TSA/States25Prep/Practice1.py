def check_common_substring(word1 = input("First word: "), word2 = input("Second word: ")):

    flag = False

    if len(word1) < len(word2):
        for let in word1:
            for lett in word2:
                if let == lett:
                    flag = True
                    break

    else:
        for let in word2:
            for lett in word1:
                if let == lett:
                    flag = True
                    break

    if not flag:
        print("NO")
    else:
        print("YES")

check_common_substring()
