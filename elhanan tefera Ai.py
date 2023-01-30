import random

def game_result(player, computer):
    if player == computer:
        return "draw"
    elif player == "rock":
        if computer == "scissors":
            return "player"
        else:
            return "computer"
    elif player == "paper":
        if computer == "rock":
            return "player"
        else:
            return "computer"
    elif player == "scissors":
        if computer == "paper":
            return "player"
        else:
            return "computer"

print("       =================================================\n")
print("---------------------------------------------------------------\n")
print(" ======= Hello and Welcome to Rock, Paper, Scissors game! =======\n")
print("---------------------------------------------------------------\n")
print("       =================================================\n")
player_wins = 0
computer_wins = 0
draws = 0

while True:
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    player = input("=== Please Choose ROCK, PAPER, or SCISSORS: === \n ").lower()
    if player not in options:
        print("=== Invalid choice! Please try again. ===")
        continue

    result = game_result(player, computer)
    if result == "draw":
        draws += 1
        print(f"=== Draw! Both chose === {player}.")
    elif result == "player":
        player_wins += 1
        print(f" ==== You win! (*_*) === {player} beats {computer}.")
    else:
        computer_wins += 1
        print(f" === Computer wins! ====  {computer} beats {player}.")

    play_again = input("\n === Do you want to play again ? If you do please say yes/no  === \n").lower()
    if play_again == "no":
        break

print(f"\nResults: \n=== You win! (*_*) ===: {player_wins}\n=== Computer Wins ! ====: {computer_wins}\n=== Draw ===: {draws}")
