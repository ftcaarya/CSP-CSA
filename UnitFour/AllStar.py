# Enter your code here

points = int(input("Points per game? "))
rebounds = int(input("Rebounds per game? "))
assists = int(input("Assists per game? "))

if points >= 25:
    all_star = True
elif points >= 10 and rebounds >= 10 and assists >= 10:
    all_star = True
else:
    all_star = False
    
print("Is all star?", all_star)