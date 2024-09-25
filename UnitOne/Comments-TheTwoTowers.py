# Enter your code here

# Function moves n count based on parameter passed.
def move_forward(count):
    for i in range(count):
        move()
        
# Function that places the acual ball tower
def place_tower():
    for i in range(3):
        put_ball()
        move()
    turn_right()

# Function turns n count left based on parameter passed.
def left(count):
    for i in range(count):
        turn_left()
     
# Function to turn right
def turn_right():
    left(3)
    
# Neccessary movement to get in desired position
move()
turn_left()
place_tower()
move_forward(2)
turn_right()

# Place tower and get back in place
for i in range(3):
    move()
    put_ball()
    
left(2)
move_forward(3)
turn_right()