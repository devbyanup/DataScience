import random
print("Welcome to Paper Scissor rock")
game=["rock","paper","scissor"]

computer=random.choice(game)

player=input("please enter your choice:- ")
if computer==player:
    print("You win")
else :
    print("You lose")
