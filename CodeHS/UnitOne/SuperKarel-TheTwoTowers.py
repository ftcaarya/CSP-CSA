# Enter your code here

def place_first_tower():
    for i in range(3):
        put_ball()
        move()
        
move()
turn_left()
place_first_tower()
turn_right()
for i in range(2):
    move()
    
turn_right()

for i in range(3):
    move()
    put_ball()
    
turn_around()
for i in range(3):
    move()
    
turn_right()