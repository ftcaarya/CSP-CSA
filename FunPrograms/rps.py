# simple sock, paper, scissors game

import random

running = True
streak = 0
maxStreak = 0

def robot_move(num) -> str:
    if num == 1:
        return "paper"
    elif num == 2:
        return "rock"
    elif num == 3:
        return "scissors"

def user_move(answer) -> str:
    if answer == "r":
        return "rock"
    elif answer == "p":
        return "paper"
    elif answer == "s":
        return "scissors"
    
def choose_winner(user, robot) -> str:
    if user == robot:
        return "Tie"
    elif user == ("rock" and robot == "scissors") or (user == "paper" and robot == "rock") or (user == "scissors" and robot == "paper"):
        return "User Wins!"
    else:
        return "Robot Wins!"   

while running == True:
    answer = input("[r]ock, [p]aper, or [s]cissors?\n")
    robotMove = random.randint(1, 3)
    print(f'\nuser move: {user_move(answer)}\nrobot move: {robot_move(robotMove)}\n')
    winner = choose_winner(user_move(answer), robot_move(robotMove))

    print("")
    print(winner)
    if winner == "Robot Wins!":
        if streak > maxStreak:
            maxStreak = streak
        print(f'Ending streak: {streak}')
        streak = 0
        repeat = input("\nWould you like to play again? [y]es or [n]o\n")
        if repeat == "n":
            print(f'\nYour max streak was {maxStreak}')
            running = False
            break
    elif winner == "User Wins!":
        streak += 1

    print(f'\nstreak: {streak}\n')

    

    

