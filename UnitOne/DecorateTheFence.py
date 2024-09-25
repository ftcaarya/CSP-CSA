def decorate():
    while front_is_clear():
        if right_is_blocked():
            put_ball()
            if front_is_clear():
                move()
        else:
            move()


while front_is_clear():
    move()
    
turn_left()
decorate()
put_ball()