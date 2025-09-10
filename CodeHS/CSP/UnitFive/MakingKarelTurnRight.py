import math
from tkinter import Image

NUM_STREETS = 4
NUM_AVES = 4
POINT_SIZE = 3
WORLD_WIDTH = 275
WORLD_HEIGHT = 275
set_size(WORLD_WIDTH, WORLD_HEIGHT)

STREET_HEIGHT = WORLD_HEIGHT // NUM_STREETS
AVE_WIDTH = WORLD_WIDTH // NUM_AVES
PAUSE_TIME = 1000

KAREL_IMG_URL = "https://codehs.com/uploads/9657058ec012105e0c5548c917c29761"
KAREL_SIZE = STREET_HEIGHT

X_POS = 0
Y_POS = WORLD_HEIGHT - KAREL_SIZE


EAST = 0
SOUTH = math.radians(90)
WEST = math.radians(180)
NORTH = math.radians(270)

def setup_world():
    global direction, karel

    for street in range(NUM_STREETS):
        for ave in range(NUM_AVES):
            x_center = ave * AVE_WIDTH + AVE_WIDTH / 2
            y_center = street * STREET_HEIGHT + STREET_HEIGHT / 2
            dot = Circle(POINT_SIZE, x_center, y_center)
            add(dot)

    karel = Image(KAREL_IMG_URL)
    karel.set_position(X_POS, Y_POS)
    karel.set_size(KAREL_SIZE, KAREL_SIZE)
    add(karel)


    direction = EAST

def turn_left():
    global karel, direction

    if direction == EAST:
        direction = NORTH
    elif direction == WEST:
        direction = SOUTH
    elif direction == NORTH:
        direction = WEST
    elif direction == SOUTH:
        direction = EAST
    else:
        print("Error: Karel's Direction is not properly set.")
        direction = EAST

    karel.set_rotation(direction)

def turn_right():
    for i in range(3):
        turn_left()

def rotate_karel(e):
    ch = chr(e.charCode)
    if ch == 'r' or ch == 'd':
        turn_right()
    elif ch == 'l' or ch == 'a':
        turn_left()

add_key_press_handler(rotate_karel)
setup_world()