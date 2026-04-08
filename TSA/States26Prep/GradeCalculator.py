def grade_calculator():
    grades = input("Enter the grades separated by commas: ")
    grade_list = grades.replace(" ", "").split(",")
    total = 0

    for grade in grade_list:
        total += int(grade)

    average = total / len(grade_list)

    if average >= 90:
        print("Your average grade is: A")
    elif average >= 80:
        print("Your average grade is: B")
    elif average >= 70:
        print("Your average grade is: C")
    elif average >= 60:
        print("Your average grade is: D")
    else:
        print("Your average grade is: F")

    gradesBelow = len([grade for grade in grade_list if int(grade) < average])
    gradesAbove = len([grade for grade in grade_list if int(grade) > average])

    print("Number of grades below average: " + str(gradesBelow))
    print("Number of grades above average: " + str(gradesAbove))

grade_calculator()