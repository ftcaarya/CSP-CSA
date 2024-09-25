# Enter your code here

def clean_row():
    if balls_present():
        take_ball()
    while front_is_clear():
        move()
        if balls_present():
            take_ball()
            
    if balls_present():
        take_ball()
        
def reset():
    turn_around()
    while front_is_clear():
        move()
    while not_facing_north():
        turn_left()
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_left()
        
for i in range(25):
    clean_row()
    reset()
