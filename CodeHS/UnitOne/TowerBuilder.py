# Enter your code here

rowNumber = 1

def make_tower():
    turn_left()
    for i in range(3):
        put_ball()
        move()

    turn_around()
    for i in range(3):
        move()

    turn_left()

make_tower()

while front_is_clear():
    move()
    rowNumber += 1
    if (rowNumber % 2) != 0:
        make_tower()

if ((rowNumber % 2) != 0) and front_is_blocked() and no_balls_present():
    make_tower()