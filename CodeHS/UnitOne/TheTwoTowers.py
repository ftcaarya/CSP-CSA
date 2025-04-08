# Enter your code here

def move_forward(units):
    for i in range(units):
        move()
        
def left(units):
    for i in range(units):
        turn_left()
        
def turn_right():
    left(3)
    
    
def stack():
    left(1)
    for i in range(3):
        put_ball()
        move_forward(1)
    turn_right()
    
move_forward(1)
stack()
move_forward(2)
turn_right()
move_forward(3)
turn_left()
stack()

