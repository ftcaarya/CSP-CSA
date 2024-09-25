# Enter your code here

if facing_south():
    turn_around()
elif facing_west():
    turn_right()
elif facing_east():
    turn_left()
    
while front_is_clear():
    put_ball()
    move()
    
put_ball()