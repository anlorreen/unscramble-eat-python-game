import random

#list for dictionary of words
dictWords = []

#lists for calculation of scores (for both anagram and scrabble mode)
points_2 = ["d","g"]
points_3 = ["b","c","m","p"]
points_4 = ["f","h","v","w","y"]
points_5 = ["k"] 
points_8 = ["j","x"]
points_10 = ["q","z"]

#lists for anagram mode
anagrams= []
listOfPickedWords = []

#lists for scrabble mode
scrabble_wordsToCombine = []
scrabble_combinedWords = []

shuffledLetters = []

correctAnswersOfPlayer = []
correctAnswersOfPlayerForCurrentRound = []

#codes for anagram mode and scrabble mode are separated except seeding of words from dictionary
def seedWords():
	file_input = open(input("Input name of dictionary file..."))
	for line in file_input:
		word = line.strip()
		dictWords.append(word)

###############################################################################################CODES FOR ANAGRAM MODE
def anagram_clearAll():			#clears list of picking words
	listOfPickedWords.clear()	
	anagrams.clear()
	#reference: https://www.programiz.com/python-programming/methods/list/clear

def anagram_pickWords():
	listOfPickedWordsSorted = []
	listOfPickedWordsSorted.clear()
	i = 0
	while i < 3:
		aWord = random.choice(dictWords)
		aWordSorted = list(aWord)
		aWordSorted.sort()
		aWordSorted = ''.join(aWordSorted)
		for x in listOfPickedWords:
			xList = list(x)
			xList.sort()
			xList = ''.join(xList)
			listOfPickedWordsSorted.append(xList)
		if aWordSorted not in listOfPickedWordsSorted:
			listOfPickedWords.append(aWord)
			i+=1

def anagram_currentWord(i):		#unshuffled word
	word = listOfPickedWords[i]
	return word

def anagram_shuffledWord(pickedWord):
	listWord = list(pickedWord)
	random.shuffle(listWord)
	newWord = ''.join(listWord)
	return newWord

def checkAnagrams(word):
	anagrams = []
	anagrams.clear()
	noOfAnagrams = 0	#counter for how many anagrams
	for x in dictWords:
		if len(word) == len(x):
			stringListPicked = list(word)
			stringListPicked.sort()
			stringListx = list(x)
			stringListx.sort()
			if stringListPicked == stringListx:
				noOfAnagrams+=1 #counter for how many anagrams
				anagrams.append(x)
			else:
				pass
		else:
			pass
	return anagrams

def numberOfAnagrams(word):
	anagrams = []
	anagrams.clear()
	noOfAnagrams = 0  #counter for how many anagrams
	for x in dictWords:
		if len(word) == len(x):
			stringListPicked = list(word)
			stringListPicked.sort()
			stringListx = list(x)
			stringListx.sort()
			if stringListPicked == stringListx:
				noOfAnagrams+=1 #counter for how many anagrams
			else:
				pass
		else:
			pass
	return noOfAnagrams

def checkUserAnswer_Anagram(user_input,word):
	anagrams = checkAnagrams(word)
	if user_input in anagrams:
		return True
	else:
		return False

def anagram_computeScore(userInpuList):
	scrabblePoints = 0 
	for word in userInpuList:
		# compute scrabble points of a word
		for letter in word:
			if letter in points_2:
				points = 2
			elif letter in points_3:
				points = 3
			elif letter in points_4:
				points = 4
			elif letter in points_5:
				points = 5
			elif letter in points_8:
				points = 8
			elif letter in points_10:
				points = 10
			else:
				points = 1
			scrabblePoints+=points
	return scrabblePoints

def anagram_highestScore():
	highestScrabblePoints = 0
	anagramlist = []	#a list of all the anagrams
	anagramlist.clear()	#clear list for every new game
	for word in listOfPickedWords:
		anagrams = []
		anagrams.clear() #clear list for new game
		anagrams = checkAnagrams(word)
		anagramlist.extend(anagrams)
	for word in anagramlist:
		for letter in word:
			if letter in points_2:
				points = 2
			elif letter in points_3:
				points = 3
			elif letter in points_4:
				points = 4
			elif letter in points_5:
				points = 5
			elif letter in points_8:
				points = 8
			elif letter in points_10:
				points = 10
			else:
				points = 1
			highestScrabblePoints+=points
	return highestScrabblePoints

#####################################################################################################CODES FOR SCRABBLE MODE
def scrabble_pickWords():
	count = 0
	while count < 3:
		word = random.choice(dictWords)
		if word not in scrabble_wordsToCombine:
			scrabble_wordsToCombine.append(word)
			count = count + 1

def scrabble_clearWordsToCombine():
	count = 0
	while count < 3:
		scrabble_wordsToCombine.remove(scrabble_wordsToCombine[len(scrabble_wordsToCombine)-1])
		count = count + 1

def scrabble_clearCorrectAnswersOfPlayerForCurrentRound():
	count = 0
	no_of_correctAnswersForCurrentRound = len(correctAnswersOfPlayerForCurrentRound)
	while count < no_of_correctAnswersForCurrentRound:
		correctAnswersOfPlayerForCurrentRound.remove(correctAnswersOfPlayerForCurrentRound[len(correctAnswersOfPlayerForCurrentRound)-1])
		count = count + 1
	#print(correctAnswersOfPlayerForCurrentRound)

def scrabble_clearAll():
	#clear scrabble_combinedWords
	count = 0
	while count < 2:
		scrabble_combinedWords.remove(scrabble_combinedWords[len(scrabble_combinedWords)-1])
		count = count + 1
	#clear shuffledLetters
	count_2 = 0
	while count_2 < 2:
		shuffledLetters.remove(shuffledLetters[len(shuffledLetters)-1])
		count_2 = count_2 + 1
	#clear correctAnswersOfPlayer
	no_of_correct = len(correctAnswersOfPlayer)
	count_3 = 0
	while count_3 < no_of_correct:
		correctAnswersOfPlayer.remove(correctAnswersOfPlayer[len(correctAnswersOfPlayer)-1])
		count_3 = count_3 + 1

def scrabble_combineWords():
	letters = []
	shortestString = ""
	#print(scrabble_wordsToCombine)
	for word in scrabble_wordsToCombine:
		for character in word:
			if character not in letters:
				letters.append(character)
	letters.sort()
	for letter in letters:
		maxCount = 1
		for word in scrabble_wordsToCombine:
			if word.count(letter) > maxCount:
				maxCount = word.count(letter)
		shortestString = shortestString + letter*maxCount
	if shortestString not in scrabble_combinedWords:
		scrabble_combinedWords.append(shortestString)
		#print(scrabble_combinedWords)
		return False
	else:
		return True

def scrabble_shuffleLetters(index):
	lettersToShuffle = [letter for letter in scrabble_combinedWords[index]]
	random.shuffle(lettersToShuffle)
	shuffled = ""
	for letter in lettersToShuffle:
		shuffled = shuffled + letter
	shuffledLetters.append(shuffled)
	#print(shuffledLetters)

def scrabble_getWord(index):
	return shuffledLetters[index]

def scrabble_checkIfCorrect(user_input,givenString):
	def checkWord(user_input,givenString):
		lettersInInput = list(user_input)
		lettersInGivenString = list(givenString)
		for x in lettersInInput:
			for y in lettersInGivenString:
				if lettersInInput.count(x) > lettersInGivenString.count(x):
					return False
				else:
					pass		
		return True

	def checkInDict(user_input):
		for word in dictWords:
			if user_input == word:
				return True
			else:
				pass
		return False

	isInString = checkWord(user_input,givenString)
	isInDict = checkInDict(user_input)
	if isInString == True and isInDict == True:
		if user_input not in correctAnswersOfPlayerForCurrentRound:
			correctAnswersOfPlayerForCurrentRound.append(user_input)
			correctAnswersOfPlayer.append(user_input)
			return 1
		else:
			return 0
	elif isInString == False:
		return -1
	# return -2 if not in dict
	return -2

def scrabble_computeScore():
	scrabblePoints = 0 
	for word in correctAnswersOfPlayer:
		# compute scrabble points of a word
		for letter in word:
			if letter in points_2:
				points = 2
			elif letter in points_3:
				points = 3
			elif letter in points_4:
				points = 4
			elif letter in points_5:
				points = 5
			elif letter in points_8:
				points = 8
			elif letter in points_10:
				points = 10
			else:
				points = 1
			scrabblePoints = scrabblePoints + points
	return scrabblePoints

def scrabble_highestScore():
	# find all words in string	
	highestScrabblePoints = 0
	for stringOfLetters in shuffledLetters:
		wordsInString = []
		for word in dictWords:
		# check if word in string
			for letter in word:
				if word.count(letter) <= stringOfLetters.count(letter):
					isCorrect = True
				else:
					isCorrect = False
					break
			if isCorrect == True:
				wordsInString.append(word)
		pointsForRound = []
		for word in wordsInString:
			pointsForWord = 0
		# compute scrabble points of a word
			for letter in word:
				if letter in points_2:
					points = 2
				elif letter in points_3:
					points = 3
				elif letter in points_4:
					points = 4
				elif letter in points_5:
					points = 5
				elif letter in points_8:
					points = 8
				elif letter in points_10:
					points = 10
				else:
					points = 1
				pointsForWord = pointsForWord + points
			pointsForRound.append(pointsForWord)
		pointsForRound.sort()
		# get3 highest for round
		highestScrabblePoints = highestScrabblePoints + pointsForRound[len(pointsForRound)-1] + pointsForRound[len(pointsForRound)-2] + pointsForRound[len(pointsForRound)-3]
	return highestScrabblePoints
#end of for scrabble only