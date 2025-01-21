import random

"""
Chooses either 1 or 2 randomly, 
if 1 is choosen then print Heads
else print Tails
"""

# Enter your code here

num = random.randint(1, 2)

if num == 1:
    print("Heads")
else:
    print("Tails")