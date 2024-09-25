# Enter your code here

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
        move()
        turn_left()
    else:
        turn_right()
        move()
        turn_left()

for i in range(14):
    if front_is_blocked():
        jump_hurdle()
    elif front_is_clear():
        move()