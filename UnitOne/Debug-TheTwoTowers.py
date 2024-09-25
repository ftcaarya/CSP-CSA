def turn_right():
    for i in range(3):
        turn_left()

def come_down():
    for i in range(2):
        turn_left()
    move()
    move()
    turn_left()

def build_tower():
    turn_left()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()

move()
build_tower()
come_down()
move()
move()
build_tower()
move()
turn_right()