INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

# Enter your code here

def convert_height_to_meters(feet, inches):
    total = inches + (feet * 12)
    meters = round((total * .0254), 4)
    print(str(feet) + " feet, " + str(inches) + " inches = " + str(meters) + " meters")
    
convert_height_to_meters(6, 4)
convert_height_to_meters(5, 8)
convert_height_to_meters(5, 2)