import random

def getValueName(choice):
	if choice == "1":
		return "Rock"
	elif choice == "2":
		return "Paper"
	else:
		return "Scissor"
	
def makeChoice():
	print('Make your choice:')
	myChoice = input()
	if myChoice != "1" and myChoice != "2" and myChoice != "3":
		print('Brinca direito!')
		makeChoice()
	return myChoice

def didIWin(playerChoice, cpuChoice):
	if playerChoice == "Rock" and cpuChoice == "Scissor":
		return True
	elif playerChoice == "Scissor" and cpuChoice == "Paper":
		return True
	elif playerChoice == "Paper" and cpuChoice == "Rock":
		return True
	elif playerChoice == cpuChoice:
		return None
	else:
		return False

def playGame():
	print("Rock, paper or scissor?")
	print("1 - Rock \n2 - Paper\n3 - Scissor")

	myValue = makeChoice()
	myChoice = getValueName(myValue)

	cpuValue = str(random.randint(1, 4))
	cpuChoice = getValueName(cpuValue)

	print("You choose " + myChoice)
	print("Your opponent chose " + cpuChoice)

	result = didIWin(myChoice, cpuChoice)

	if result is None:
		print("Draw game :|")
	elif result:
		print("Congratulations, you won!")
	else:
		print("Holy hamburguers, you lost!")
	
	print("Play again? \nY - 'Yeah, sure!'\nN - I'm outta here")
	playAgain = input()
	
	if playAgain.lower() == "y":
		playGame()	

playGame()