# import random package so tat we can generate a random choice
from random import randint

#set up variables for players and AI lives
player_lives = 5
computer_lives = 5

# choices is n array => an array is a container these   hat can hold multiple values
choices = ["rock", "paper" , "scissors"]

# set a computer variable to one of these choices
computer = choices[randint(0,2)]


# set up the game loop so that we don't have to restart all te time 
player = False

while player is False:
	#set player true
	print("**************************************\n")
	print("computer lives: ", computer_lives, "/5\n")
	print("player lives: ", player_lives, "/5\n")
	print("choose your weapon!\n\n")
	print("**************************************\n")

	player = input("choose rock, paper or scissor\n")
	player = player.lower()

	print("computer choose:", computer, "\n")

	print("player choose:", player, "\n")

	if player == "quit":
		exit()
	
	elif computer == player:
	   print("tie! no one wins, play again")
	elif player == "rock":
		if computer == "paper":
			print("you lose!", computer, "covers", player, "\n" )
			player_lives = player_lives - 1

		else:
			print("you win!", player, "covers", computer, "\n")
			player_lives = player_lives - 1
	elif player == "paper":
		if computer == "scissors":
			print("you lose!", computer, "covers", player, "\n" )
			player_lives = player_lives - 1

		else:
			print("you win!", player, "covers", computer, "\n")
			player_lives = player_lives - 1


	elif player == "scissors":
		if computer == "rock":
			print("you lose!", computer, "smashes", player, "\n" )
			player_lives = player_lives - 1

		else:
			print("you win!", player, "cuts", computer, "\n")
			player_lives = player_lives - 1

	else:
		print("thats not a valid choice, try again")


	# handle all lives lost for player or AI
	if player_lives is 0:
		print("out of lives! you suck at this game. Would you like to play again?\n")
		choice = input("Y / N")
		print(choice) 

		if (choice is "N") or (choice is "n"):
			print("you chose to quit")
			exit()

		elif (choice is "Y") or (choice is "y"):
			# reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5 
			player = False 
			computer = choices[randint(0, 2)]

	elif computer_lives is 0:
		print("out of lives! you suck at this game. Would you like to play again?\n")
		choice = input("Y / N")
		print(choice) 

		if (choice is "N") or (choice is "n"):
			print("you chose to quit")
			exit()

		elif (choice is "Y") or (choice is "y"):
			# reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5 
			player = False 
			computer = choices[randint(0, 2)]


	
	else:
		#need to check all of our conditions after checking for a tie
		player = False 
		computer = choices[randint(0, 2)]
