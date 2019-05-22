import random

isPlaying = True
answer = random.randint(0, 9)
guessCount = 0
playerGuess = 0

# Play until the user can play no longer
while isPlaying:
	# Only show the initial prompt once a game.
	if guessCount == 0:
		playerGuess = raw_input("I'm thinking of a number between 0-9... Guess!\n")
	
	# Track how many times we have been in this loop
	guessCount += 1
	
	## Check for user error.
	# Use must input a number. This could have been done in a try/catch, but those are expensive.
	if playerGuess.isdigit() == False:
		playerGuess = raw_input("Your guess must be a whole number between 0-9.\nTry again!\n")
		continue
	
	# If the input was a number... Check to see if the number was in range, and if the guess was correct
	playerGuessAsInt = int(playerGuess)
	if playerGuessAsInt < 0 or playerGuessAsInt > 9:
		playerGuess = raw_input("Your guess must be a whole number between 0-9.\nTry again!\n")
		continue
	elif playerGuessAsInt != answer:
		playerGuess = raw_input("Close, but not close enough. \nTry again!\n")
		continue;
	
	print "Winner! You guessed in", guessCount, "tries! Woo!\n\n";
	
	# Reset the game in the event the user wants to play again.
	answer = random.randint(0, 9)
	guessCount = 0

	# Ask the user if they want to play again. Exit the game loop if they don't
	while True:
		playAgainInput = raw_input("Want to play again? (y/n) ")
		if playAgainInput == 'n':
			isPlaying = False
			break;
		elif playAgainInput == 'y':
			isPlaying = True
			break;
	
	