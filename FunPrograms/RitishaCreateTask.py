import random

arms = ["curls", "push-ups", "pull-ups", "dips"]
legs = ["squats", "lunges", "calf raises", "leg press"]
core = ["planks", "sit-ups", "leg raises", "Russian twists"]

def generate_workout(type_of_workout):
    if type_of_workout == "arms" and len(arms) > 0:
        chosen = random.choice(arms)
        arms.remove(chosen)
        return chosen
    elif type_of_workout == "legs" and len(legs) > 0:
        chosen = random.choice(legs)
        legs.remove(chosen)
        return chosen
    elif type_of_workout == "core" and len(core) > 0:
        chosen = random.choice(core)
        core.remove(chosen)
        return chosen  
    else:
        return None

choice = input("Choose a workout routine (arms, legs, core): ").strip().lower()
while choice not in ["arms", "legs", "core"]:
    choice = input("Invalid choice. Please choose from (arms, legs, core): ").strip().lower()

random_workout = generate_workout(choice)

if random_workout == None:
    print(f"You have depleted the list of {choice} workouts!")
else:
    print(f"Your random {choice} workout is: {random_workout}")

repeat = input("Would you like to generate another workout? (yes/no): ").strip().lower()

while repeat == "yes":
    random_workout = generate_workout(choice)
    if random_workout == None:
        print(f"You have depleted the list of {choice} workouts!")
    else:
        print(f"Your random {choice} workout is: {random_workout}")
    repeat = input("Would you like to generate another workout? (yes/no): ").strip().lower()
else:
    print("Thank you for using the workout generator!")