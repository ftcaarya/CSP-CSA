def turn_right():
    for i in range(3):
        turn_left()

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(5):
    for i in range(2):
        move()
    jump_hurdle()