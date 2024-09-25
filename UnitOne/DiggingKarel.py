# Enter your code here

def turn_right():
    for i in range(3):
        turn_left()

def bury_call():
    for i in range(3):
        for i in range(2):
            move()
        turn_right()
        for i in range(3):
            move()
        put_ball()
        for i in range(2):
            turn_left()
        for i in range(3):
            move()
        turn_right()
        move()
        
bury_call()