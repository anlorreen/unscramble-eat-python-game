import time
import engine
import os

def clr():
	os.system('cls' if os.name == 'nt' else 'clear')
#reference: youtube comment by Krystle Kirk
 
#this is the interface proper
def playGame():

	##################################################################################################GAMEPLAY CODE FOR ANAGRAM WITH RETRIES
	def anagramWithRetries():
		userInputList = []
		userInputList.clear()
		engine.anagram_pickWords()
		i = 0	#index for picking words in Anagram mode and displaying round
		while i < 3:
			correctCounter = 0
			mistakeCounter = 0
			word = engine.anagram_currentWord(i)
			n = engine.numberOfAnagrams(word)
			nCounter = n	#number of anagrams left for each correct answer
			shuffled = engine.anagram_shuffledWord(word)
			while correctCounter < n and mistakeCounter < 4:
				displayWordAnagram(i, shuffled)
				user_input = input("Enter answer:")
				user_input = user_input.lower()
				if user_input == '':
					if n == nCounter:
						clr()
						printWithSuperMinorBorder("Not a real word! Please try again.\nCount of invalid answers for this round: "+ str(mistakeCounter)+"\nNumber of Anagrams left: "+ str(n))
						input("Press enter...")
					else:
						clr()
						printWithSuperMinorBorder("Not a real word! Please try again.\nCount of invalid answers for this round: "+ str(mistakeCounter)+"\nNumber of Anagrams left: "+ str(nCounterForOthers))
						input("Press enter...")
				elif engine.checkUserAnswer_Anagram(user_input,word) == True:
					if user_input not in userInputList:
						userInputList.append(user_input)
						clr()
						correctCounter+=1
						nCounter-=1
						nCounterForOthers = nCounter	#counter for remaining anagrams for other outcomes
						printWithSuperMinorBorder("CORRECT!!! \nCount of correct for this round: "+ str(correctCounter)+"\nNumber of Anagrams left: "+ str(nCounter))
						input("Press enter...")
					else:
						clr()
						printWithSuperMinorBorder("You've already entered that word!!! \nCount of invalid answers for this round: "+ str(mistakeCounter)+"\nNumber of Anagrams left: "+ str(nCounterForOthers))
						input("Press enter...")
				else:
					if n == nCounter:
						clr()
						mistakeCounter+=1
						printWithSuperMinorBorder("WRONG!!! \nCount of invalid answers for this round: "+ str(mistakeCounter)+"\nNumber of Anagrams left: "+ str(n))
						input("Press enter...")
					else:
						clr()
						mistakeCounter+=1
						printWithSuperMinorBorder("WRONG!!! \nCount of invalid answers for this round: "+ str(mistakeCounter)+"\nNumber of Anagrams left: "+ str(nCounterForOthers))
						input("Press enter...")
				if mistakeCounter == 4:
					clr()
					printUpperMajorBorder()
					print()
					printAlignToVertices("GAME OVER!!!")
					print()
					printBottomMajorBorder()
					input("Press enter...")
					i = 2
					break	
			i+=1
		score = engine.anagram_computeScore(userInputList)
		highestScore = engine.anagram_highestScore()
		clr()
		printLoading2("score")
		if score == highestScore:
			clr()
			printUpperMajorBorder()
			print()
			print("CONGRATULATIONS!!".center(60))
			print()
			printBottomMajorBorder()
			input("Press enter...")
		else:
			pass
		clr()
		printWithMajorBorder("You scored " +str(score)+" point(s).\nHighest possible score for this game is "+str(highestScore)+".")
		input("Press enter...")
		engine.anagram_clearAll()

	##################################################################################################GAMEPLAY CODE FOR SCRABBLE WITH RETRIES
	def scrabbleWithRetries():
		engine.scrabble_pickWords()
		repeat = engine.scrabble_combineWords()
		engine.scrabble_clearWordsToCombine()

		engine.scrabble_pickWords()
		repeat = engine.scrabble_combineWords()
		engine.scrabble_clearWordsToCombine()
		while repeat == True:
			engine.scrabble_pickWords()
			repeat = engine.scrabble_combineWords()
			engine.scrabble_clearWordsToCombine()

		count = 0	
		while count < 2:
			engine.scrabble_shuffleLetters(count)
			count = count + 1

		count_2 = 0
		while count_2 < 2:
			countOfWrong = 0
			countOfCorrect = 0
			while countOfCorrect < 3 and countOfWrong < 4:
				givenString = displayWordScrabble(count_2)
				user_input = input("Enter answer: ")
				user_input = user_input.lower()
				isCorrect = engine.scrabble_checkIfCorrect(user_input,givenString)
				# isCorrect == 1 means is correct; isCorrect == -1 means not in string; isCorrect == 0 means already answered; isCorrect == -2 means not in dict
				if isCorrect == 1:
					clr()
					countOfCorrect = countOfCorrect + 1
					printWithSuperMinorBorder("CORRECT!!! \nCount of correct for this round: "+ str(countOfCorrect))
					input("Press enter...")
				elif isCorrect == 0:
					clr()
					printWithSuperMinorBorder("You've already entered that word!!! \nCount of invalid answers for this round: "+ str(countOfWrong))
					input("Press enter...")
				elif isCorrect == -1:
					clr()
					countOfWrong = countOfWrong + 1
					printWithSuperMinorBorder("Word is not in string!!! \nCount of invalid answers for this round: "+ str(countOfWrong))
					input("Press enter...")
				else:
					clr()
					countOfWrong = countOfWrong + 1
					printWithSuperMinorBorder("Oops! Either the word that you entered is not a real word, \nor it is simply not in the dictionary. \nCount of invalid answers for this round: "+ str(countOfWrong))
					input("Press enter...")
			engine.scrabble_clearCorrectAnswersOfPlayerForCurrentRound()
			if countOfWrong == 4:
				clr()
				printUpperMajorBorder()
				print()
				printAlignToVertices("GAME OVER!!!")
				print()
				printBottomMajorBorder()
				input("Press enter...")
				break					
			count_2 = count_2 + 1
		score = engine.scrabble_computeScore()
		highestScore = engine.scrabble_highestScore()
		clr()
		printLoading2("score")
		clr()
		printWithMajorBorder("You scored " +str(score)+" point(s).\nHighest possible score for this game is "+str(highestScore)+".")
		input("Press enter...")
		#clear all lists except for dictWords
		engine.scrabble_clearAll()
		
	def printMenu():
		clr()
		printUpperMajorBorder()
		print()
		printAlignToVertices("MENU")
		print()
		printSuperMinorBorder()
		print("For ANAGRAM MODE  [Press 1]") 
		print("For SCRABBLE MODE [Press 2]")
		printSuperMinorBorder()
		print()
		printBottomMajorBorder()
		

	printMenu()
	user_option = input("Enter choice...")
	clr()
	while user_option != "1" and user_option != "2":
		printMenu()
		user_option = input("Enter choice...")
		clr()
	if user_option == "1":
		pass
		anagramWithRetries()
	else:
		scrabbleWithRetries()
	

#design components and formatting
def printUpperMajorBorder():
	no_of_spaces = 0
	no_of_not_space = 5

	padding = " "*no_of_spaces
	not_space = "|"*no_of_not_space
	invertedTriangle = padding + not_space + padding

	while no_of_not_space >= 1:
		print(invertedTriangle*12)
		no_of_not_space = no_of_not_space- 2
		no_of_spaces = no_of_spaces + 1
		padding = " "*no_of_spaces
		not_space = "+"*no_of_not_space
		invertedTriangle = padding + not_space + padding

def printBottomMajorBorder():
	no_of_spaces = 2
	no_of_not_space = 1

	padding = " "*no_of_spaces
	not_space = "+"*no_of_not_space
	Triangle = padding + not_space + padding

	while no_of_not_space < 5:
		print(Triangle*12)
		no_of_not_space = no_of_not_space + 2
		no_of_spaces = no_of_spaces - 1
		padding = " "*no_of_spaces
		not_space = "+"*no_of_not_space
		Triangle = padding + not_space + padding

	padding = " "*no_of_spaces
	not_space = "|"*no_of_not_space
	Triangle = padding + not_space + padding
	print(Triangle*12)

def printSuperMinorBorder():
	print("="*60)

def printAlignToVertices(text):
#applicable only to strings of even length with max size 12		
	no_of_spaces = 2
	no_of_not_space = 1

	padding = " "*no_of_spaces
	not_space = "+"*no_of_not_space

	printText = " "*(int((12-len(text))/2)*5)
	for letter in text:
		printText= printText + padding + letter + padding
	printText = printText + " "*20
	print(printText)

def printWithSuperMinorBorder(text):
	printSuperMinorBorder()
	print()
	print(text)
	print()
	printSuperMinorBorder()

def printWithMajorBorder(text):
	printUpperMajorBorder()
	print()
	print(text)
	print()
	printBottomMajorBorder()
# end of design components and formatting

#name of game and instructions
def printNameOfGame():
	printUpperMajorBorder()
	printSuperMinorBorder()
	print()
	print()

	printAlignToVertices("UNSCRAMBLE")
	print()
	printAlignToVertices("EAT")

	print()
	print()
	printSuperMinorBorder()
	printBottomMajorBorder()
	input("Press enter...")
	clr()

def printInstructions():
	printUpperMajorBorder()
	print()
	printAlignToVertices("INSTRUCTIONS")
	print()
	printSuperMinorBorder()
	print("ANAGRAM MODE")
	print()
	print("The are 3 rounds for this game mode. Player is allowed")
	print("3 mistakes per round. Player may only enter the next round")
	print("once all the anagrams of the given string has been guessed.")
	print()
	print("Scores are computed by the value of characters in each")
	print("anagram entered. Highest possible score can be attained")
	print("when the player successfully enters all the anagrams of the")
	print("given string for each round.")
	printSuperMinorBorder()
	print("SCRABBLE MODE")
	print()
	print("There are 2 rounds for this game mode. Player is allowed")
	print("3 mistakes per round. Player may only enter the next round")
	print("once player guesses 3 valid words that are both in the")
	print("given string and in the dictionary file.")
	print()
	print("Scores are based on the scrabble points of the letters of")
	print("the correct answers. Highest possible score can be attained")
	print("when the player guesses 3 words that have the highest")
	print("scrabble points.")
	printSuperMinorBorder()
	printBottomMajorBorder()
	input("Press enter...")
	clr()

#display interface code for Anagram mode
def displayWordAnagram(index, word):
	   clr()
	   printUpperMajorBorder()
	   print()
	   printAlignToVertices("ANAGRAM")
	   print()
	   printSuperMinorBorder()
	   round = str(index + 1)
	   print(round.center(60,"*"))
	   printSuperMinorBorder()
	   print()
	   givenString = word
	   print(givenString.center(60).upper())
	   #source: www.programiz.com
	   print()
	   printSuperMinorBorder()
	   print(round.center(60,"*"))
	   printSuperMinorBorder()
	   print()
	   printBottomMajorBorder()
	   return givenString

#display interface code for Scrabble mode
def displayWordScrabble(index):
	clr()
	printUpperMajorBorder()
	print()
	printAlignToVertices("SCRABBLE")
	print()
	printSuperMinorBorder()
	round = str(index + 1)
	print(round.center(60,"*"))
	printSuperMinorBorder()
	print()
	givenString = engine.scrabble_getWord(index)
	print(givenString.center(60).upper())
	#source: www.programiz.com
	print()
	printSuperMinorBorder()
	print(round.center(60,"*"))
	printSuperMinorBorder()
	print()
	printBottomMajorBorder()
	return givenString


# special effects
def printLoading2(what):
	clr()
	count = 1
	start_time = time.time()
	while time.time()-start_time <= 2.5:
		time2 = time.time()
		print("Loading "+what+"...")
		print(("*"*10+"  ")*count)
		print(("*"*10+"  ")*count)
		print(("*"*10+"  ")*count)
		print(("*"*10+"  ")*count)
		while time.time() -time2 < .5:
			if time.time() - time2 < .5:
				pass
		clr()
		count = count + 1
	clr()










