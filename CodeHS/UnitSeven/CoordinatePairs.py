import math

def distance(first_point, second_point):
    dif1 = pow(abs(first_point[0] - second_point[0]), 2)
    dif2 = pow(abs(first_point[1] - second_point[1]), 2)
    return math.sqrt(dif1 + dif2)