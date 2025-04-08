"""
 This program has Karel paint a checkerboard
"""

def paint_row():
    for i in range(8):
        paint(color['black'])
        if front_is_clear():
            move()
        paint(color['red'])
        if front_is_clear():
            move()
            
def reset():
    while not_facing_north():
        turn_left()
    if front_is_clear():
        move()
    if left_is_blocked():
        turn_right()
    elif right_is_blocked():
        turn_left()
        
for i in range(8):
    paint_row()
    reset()
    
turn_right()
for i in range(7):
    move()
turn_left()