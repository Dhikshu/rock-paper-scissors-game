##rock paper scissors game
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print(" win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print(" win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("lost", computer, "smashes", player)
            cpu_score+=1
        else:
            print("win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
