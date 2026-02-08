def is_leap_year(year):
    if year < 1582:
        if (year % 4 == 0):
            print("LEAP")
        else:
            print("COMMON")
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("LEAP")
        else:
            print("COMMON")
    

if __name__ == "__main__":
    year = int(input())
    is_leap_year(year)