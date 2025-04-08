def factorial(n):
    # Initialize an empty list to store the sequence
    seq = [1]
    
    # Iterate through all numbers from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Calculate the next number in the sequence by multiplying the current number with its previous value
        next_num = seq[i-2] * i
        # Append the new number to the sequence list
        seq.append(next_num)
    
    print("Factorial sequence up till the " + str(n) + "-th term is: ", seq)
    
    return seq[-1]

# Ask the user for which term in the factorial number sequence they want.
n = int(input("Which term in the factorial number sequence would you like to check? "))

print("The " + str(n) + " factorial number is: ", factorial(n))