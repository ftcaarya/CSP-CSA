# This graphics program should draw a square. 
# The fill color should be randomly choosen from
# the COLORS list

import random

set_size(480, 400)

SIDE_LENGTH = 100
COLORS = [Color.red, Color.orange, Color.yellow, Color.green, Color.blue, 
        Color.purple, Color.black, Color.gray]
        
square = Rectangle(SIDE_LENGTH, SIDE_LENGTH)
square.set_color(random.choice(COLORS))
square.set_posistion(100, 100)
add(square)