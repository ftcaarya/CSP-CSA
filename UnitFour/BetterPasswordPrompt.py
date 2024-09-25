# Enter your code here

SECRET = "abc123"
password = ""

while password != SECRET:
    password = input("Enter password: ")
    if password != SECRET:
        print("Sorry, that did not match. Please try again.")
    else:
        print("You got it!")
        break