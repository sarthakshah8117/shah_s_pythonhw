#define python function that takes argument......
def winorlose(status):
	print("called win or lose")
	print("****************")

	print("you" status, "!would you like to play again?")

	choice = input("Y / N")
		print(choice) 

		if (choice is "N") or (choice is "n"):
			print("you chose to quit")
			exit()

		elif (choice is "Y") or (choice is "y"):
			# reset the game so that we can start all over again
			global computer_lives
			global player_lives
			global player
			global computer
			global choices

			player_lives = 1
			computer_lives = 1 
			player = False 
			computer = choices[randint(0, 2)]

