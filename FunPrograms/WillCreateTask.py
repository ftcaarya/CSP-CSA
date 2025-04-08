def factorial(n):
    # List that stores all the base case shifts and records the entire sequence up till the n-th number
    seq = [1]

    # Base case sort of a sliding window to help calculate next number in the sequence
    base = [1]

    # Return if number is the initial base case
    if n == 0:
        return base[n]

    # Iterate through the sequence, every 2 step due to the size of our sliding window list, until we reach the number of our choice
    for i in range(2, n + 1):
        # Slide the window list over as we iterate through the sequence order
        base[0], base[1] = base[1], base[0] * (i + 1)

        # Add new calculate number to the list of the entire sequence.
        seq.append(base[1])

    # Print the entire sequence up till the n-th number
    print(f"Factorial sequence up till the {n}-th term is: {seq}")

    # Return the n-th number of the sequence
    return base[1]

# Ask the user for which term in the factorial number sequence they want.
factorial_num = int(input("Which term in the factorial number sequence would you like to check? "))

# Prints the return value of the factorial function which is just the term in the factorial sequence that the user desires
print("The " + str(factorial_num) + " factorial number is " + str(factorial(factorial_num)))