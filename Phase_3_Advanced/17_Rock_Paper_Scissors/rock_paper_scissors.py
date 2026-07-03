"""
Project 17: Rock, Paper, Scissors
External Requirements: None
"""
import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in choices:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = choices[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_score += 1
    elif user_input == computer_pick:
        print("Draw!")
    else:
        print("You lost!")
        computer_score += 1

print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")
