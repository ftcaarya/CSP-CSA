# This function has karel move across a world of 14 columns, moving if the
# front is clear, or jumping a hurdle if it is blocked.

# This function has karel jump a hurdle and end up on the other side.
# Precondition: Karel is facing east in front of a hurdle (one wall high)
# Postcondition: Karel is facing east on the other side of the hurdle

def turn_right():
    for i in range(3):
        turn_left()

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