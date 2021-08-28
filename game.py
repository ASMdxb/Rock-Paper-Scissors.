#Rock, Paper and Scissors:

import random

#User choice and computer choice:

while True:
    user_action = input("Enter a Choice (rock, paper, scissors): ")
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possible_actions)
    if user_action not in possible_actions:
        print("Enter a valid choice")
        continue
    print(f"\nYou Chose {user_action}, Computer Chose {computer_action}")

#Game Decision:

    print("Play!")
    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("You Lose!")
            break
        else:
            print("You Win!")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("You Lose!")
            break
        else:
            print("You Win!")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("You Lose!")
            break
        else:
            print("You Win!")
