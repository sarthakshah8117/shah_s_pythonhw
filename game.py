# import random package so tat we can generate a random choice
from random import randint

# choices is n array => an array is a container these   hat can hold multiple values
	choices = ["rock", "paper" ,"scissors"]

# set a computer variable to one of these choices
computer = choices[randint(0,2)]

player = input("choose rock, paper or scissors\n")
# set up the game loop so that we don't have to restart all te time 
player = False

while player = False:
	#set player true
	player = input("choose rock, paper or scissor\n")

	print("computer choose:", computer, "\n")

	print("player choose:", player, "\n")
	if player== "quit":
		exit()
		elif("tie! no one wins, play again")





#need to check all of our conditions after checking for a tie
player = False 
computer = choices[randint(0, 2)]