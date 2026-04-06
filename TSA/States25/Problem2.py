def palindrome(s = input("Please enter a value to be checked: ")):
    orig = s
    # alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if "?" in s:
        s = s[0:s.index("?")] + s[s.index("?") + 1:]

    if "!" in s:
        s = s[0:s.index("!")] + s[s.index("!") + 1:]

    if "," in s:
        s = s[0:s.index(",")] + s[s.index(",") + 1:]

    if "." in s:
        s = s[0:s.index(".")] + s[s.index(".") + 1:]

    i = 0
    while i < len(s):
        value = s[i]
        if value == " ":
            s = s[0:i] + s[i + 1:]
            i = 0
        else:
            i += 1


    # if " " in s:
    #     s = s[0:s.index(" ")] + s[s.index(" ") + 1:]
    # print(s.index("?"))
    # s.index(".")
    # s.index("!")
    # s.index("...")

    # print(s.lower())
    # print(s.lower()[::-1])

    if s.lower() == s.lower()[::-1]:
        print(f"Results: {orig} is a palindrome.")
    else:
        print(f"Results: {orig} isn't a palindrome.")


palindrome()