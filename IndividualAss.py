import random

# initialize variables to keep track of wins, losses, and draws
user_wins = 0
computer_wins = 0
draws = 0

while True:
    # get user's choice
    user_choice = input("Please choose rock, paper, or scissors: ").lower()
    # validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue
    # generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    # compare choices and determine winner

    if user_choice == computer_choice:
        draws += 1
        print("It's a draw!")
         # winning conditions: r > s, s > p, p > r
    elif user_choice == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("You win! Rock beats scissors.")
    elif user_choice == "paper" and computer_choice == "rock":
        user_wins += 1
        print("You win! Paper beats rock.")
    elif user_choice == "scissors" and computer_choice == "paper":
        user_wins  += 1
        print("You win! Scissors beats paper.")
    else:
        computer_wins += 1
        print("You lose!")
    # ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break

# print game statistics
print(f"User wins : {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Draws: {draws}")