# Enter your code here

rowNumber = 1

def make_tower():
    turn_left()
    for i in range(3):
        put_ball()
        move()
<<<<<<< HEAD:UnitOne/TowerBuilder.py
        
    turn_around()
    for i in range(3):
        move()
=======

    turn_around()
    for i in range(3):
        move()

>>>>>>> d108d2e3eb179eca1bfe3ad78abe0a4970f4af0f:CodeHS/UnitOne/TowerBuilder.py
    turn_left()

make_tower()

while front_is_clear():
    move()
    rowNumber += 1
    if (rowNumber % 2) != 0:
        make_tower()
<<<<<<< HEAD:UnitOne/TowerBuilder.py
        
=======

>>>>>>> d108d2e3eb179eca1bfe3ad78abe0a4970f4af0f:CodeHS/UnitOne/TowerBuilder.py
if ((rowNumber % 2) != 0) and front_is_blocked() and no_balls_present():
    make_tower()