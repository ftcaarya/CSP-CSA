"""
This program has Karel invert colors
"""

for i in range(10):
    if color_is(color['blue']):
        paint(color['red'])
        
    else:
        paint(color['blue'])
        
    if front_is_clear():
        move()