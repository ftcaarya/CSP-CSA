# This program will have Karel run around the racetrack

# Enter your code here

def race():
    for i in range(32):
        while front_is_clear():
            move()
            if front_is_blocked():
                put_ball()
        turn_left()


race()