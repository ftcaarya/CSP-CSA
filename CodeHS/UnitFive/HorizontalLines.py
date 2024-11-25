# Write a function to draw a horizontal
# line given a y position and a length

def horizontal_line(y, length):
    line = Line(0, y, length, y)
    add(line)

horizontal_line(100, 200)
horizontal_line(200, 100)
horizontal_line(300, 20)