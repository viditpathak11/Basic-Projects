#A simple implementation of the classic "Rock-Paper-Scissor" game using the random library in python.

from random import randint
 '''This is a simple Rock Paper Scissor Game using nested conditional statements'''
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
 
#assign a random play to the computer
computer = t[randint(0,2)]
 
#set player to False
player = "Yes"
count=3
 
while player == "Yes" and count>0:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = "Yes"
    computer = t[randint(0,2)]
    count=count-1
