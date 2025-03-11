def tsaAttendance(weeks = int(input("Number of Weeks: "))):
    total = []
    for week in range(weeks):
        currentWeek = week + 1
        tempList = input(f"Week {currentWeek} Attendance: ").split(" ")
        for item in tempList:
            total.append(item)

        tempList.clear()

    max = []
    maxCount = 0
    for i in total:
        if total.count(i) >= maxCount and total.count(i) not in max:
            max.append(i)
            maxCount = total.count(i)

    max = sorted(list(set(max)))
    print(f"Best Attendance: {" ".join(max)}, {total.count(max[0])} meetings")

tsaAttendance()



