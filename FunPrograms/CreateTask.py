# Define a function for printing the fibonacci sequence with a parameter of n
def fib(n):
    # List that stores all the base case shifts and records the entire sequence up till the n-th number
    seq = [0, 1]

    # Base case, sliding window to help calculate next number in the sequence.
    base = [0, 1]

    # Return if number is initial base case
    if n < 2:
        return base[n]

    # Iterate through the sequence, every 2 step due to the size of our sliding window list, until we reach the number of our choice
    for i in range(2, n + 1):
        # Slide the window list over as we iterate through the sequence order
        base[0], base[1] = base[1], sum(base)

        # Add new calculate number to the list of the entire sequence.
        seq.append(base[1])

    # Print the entire sequence up till the n-th number
    print(f"Fibonacci sequence up till the {n}-th term is: {seq}")

    # Return the n-th number of the sequence
    return base[1]


# Ask the user for which term in the fibonacci number sequence they want.
fib_num = int(input("Which term in the fibonacci number sequence would you like to check? "))

# Prints the return value of the fib function which is just the term in the fibonacci sequence that the user desires
print(f"The {fib_num} fibonacci number is {fib(fib_num)}")