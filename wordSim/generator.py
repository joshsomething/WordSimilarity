'''	Copyright 2018 Joshua Danielpour


	This file is part of WordSimilarity.

    WordSimilarity is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    WordSimilarity is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with WordSimilarity.  If not, see <http://www.gnu.org/licenses/>.
    
'''
from sklearn.externals import joblib
model = joblib.load("wordsim.pkl")
import numpy as np
from random import random
#strategy: don't actually use a real generative model,
#just make random (slight-ish) changes, predict what 
#similarity we think we'll get, and make changes to the model to
#adjust what a human would rate

def getChance(threshhold):
	return random() < threshhold
#get a choice from range [start/0, end], skewed to start
def skewedChoice(start=0, end):
	size = end - start + 1
	weights = reversed[.1 * (x + 1) for x in reversed(range(size))]
	#credit to answerer (Michael Madsen) from https://gamedev.stackexchange.com/questions/6043/algorithm-for-determining-random-events
	#for rest of code in this function (skewedChoice):
	weightSum = sum(weights)
	randomNum = random() * weightSum
	T=0
	for i in range(start=0, end):
		T += weights[i]
		if (T > randomNum):
			return i
	return -1
	#end function

def randChar():
	return chr(([i for i in range(ord('0'), ord('9') + 1)] + [z for z in range(ord('a'), ord('z') + 1)])[int( random() * (ord('9') - ord('0') + ord('z') - ord('a') + 2 ) )])

def getSubList(firstVal, listy):
	for subList in listy:
		if (firstVal == subList[0]):
			return subList
	return [-1, -1]

def generate(word):
	if (len(word) < 2):
		raise("word too short")
	removeChars = getChance(.1) #10% chance to remove a character
	numRemoves = 0
	if (len(word) == 2):
		numRemoves = 1
	elif (len(word) == 3):
		if (removeChars):
			numRemoves = skewedChoice(1, len(word) - 2)
	elif (removeChars):
		numRemoves = skewedChoice(1, len(word) - 3)
	
	start = 1
	if (numRemoves > 0):
		start = 0
	numChanges = skewedChoice(start, len(word) - (1 + numRemoves))
	
	changes = [[None, None]]
	if (numChanges > 0):
		changes = [ [int(random() * len(word)), ord(randChar())] ]
	
	removes = []
	proccessed = [1, 0]
	while True:
		if (proccessed[0] >= numChanges and proccessed[1] >= numRemoves):
			break
		elif (proccessed[0] < numChanges):
			index = int(random() * len(word))
			if (getSubList(index, changes)[0] < 0 
			and index not in removes):
				changes.append(index, ord(randChar()))
				proccessed[0] += 1
		if (proccessed[1] < numRemoves):
			index = int(random() * len(word))
			if (getSubList(index, changes)[0] < 0 
			and index not in removes):
				removes.append(index, ord(randChar()))
				proccessed[1] += 1
	
	changedWord = ""
	for i in xrange(len(word)):
		if (i not in removes):
			val = getSubList(i, changes)[1]
			if (val >= 0):
				changedWord += chr(val)
			else:
				changedWord += word[i]
		
	return changedWord
		
def combineData(dataset):
	biggerDf = pd.read_csv('wordsim.csv')
	totalDataset = {'Pairs': biggerDf.loc['Pairs'] + dataset['Pairs'], 
	'Similarities': biggerDf.loc['Similarities'] + dataset['Similarities']}
	return pd.DataFrame(totalDataset, columns=['Pairs', 'Similarities'])

def retrain(df):
	#get pairs and y.
	pairs = df.loc['Pairs']
	y = df.loc['Similarities']

	#turn the Pairs into a whole lot of numbers:
	X = [UnevenWordPair(pairs[i][0], pairs[i][1]).getFinalArrangement() for i in range(len(pairs))]

	#split half the data for the algorithm to learn from,
	#half to test the results later:
	from sklearn.model_selection import train_test_split  
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4) #40% of the word pairs will be just for tests test



	
	#for the moment of truth, now for the actual learning!
	from sklearn.neural_network import MLPRegressor
	#reuse our model:
	mlp = model 

	#do your work, complicated math!
	mlp.fit(X_train, y_train)

	#evaluate the results:
	#get the predictions out of the testing data:
	y_predicted = mlp.predict(X_test)

	#get the average error:
	from sklearn.metrics import mean_absolute_error 
	absErr = mean_absolute_error(y_test, y_pred)
	debug = ["Error rate (mean): " + str(absErr),
	"Predicted y values: " + "[" + ", ".join( str(x) for x in y_predicted) + "]",
	"Real y values: " + "[" + ", ".join( str(x) for x in y_test) + "]",
	"Predicted y values: " + "[" + ", ".join( str(x) for x in y_predicted) + "]"]

	#open file to save the scoring:
	f = open('tunedwordsim.out', 'ab') #append mode

	#print info about testing results:
	for line in debug:
	print(line)
	f.write(line)

	f.close() #close file

	#make sure to keep track of sklearn's version:
	from sklearn import __version__ as sk_ver
	f = open('sklearn_version', 'w')
	f.write(sk_ver)
	f.close()

	#now export this good stuff!
	from sklearn.externals import joblib
	joblib.dump(mlp, 'tunedwordsim.pkl')

def askedForHelp(string):
	return string.find('\h') >= 0 and string.find('\\\h') < 0
def getWord(message="Enter a word: "):
	getAWord = ""
	while (True):
		trial = input(message)
		if (askedToLeave(trial)):
			return '\q'
		if (wordShouldChange(trial)):
			continue
		if (askedForHelp(trial)):
			printHelpfullness()
		else:
			return trial
def wordShouldChange(string):
	return string.find('\w') >= 0 and string.find('\\\w') < 0
def askedToLeave(string):
	return string.find('\q') >= 0 and string.find('\\\q') < 0
def printHelpfullness(message='Generator: \nEnter \'\h\' get help instructions.\n Enter \'\w\' to change your word. \nEnter \'\q\' to finish.'):
	print(message)
	time.sleep(.8)
def displayPair(one, two):
	print("Entered word: " + one)
	print("Created word: " + two)
def getSim():
	while (True):
		sim = input("Rate the similarity: ")
		if (askedToLeave(sim)):
			return '\q'
		if (wordShouldChange(sim)):
			return '\w'
		if (askedForHelp(sim)):
			printHelpfullness()
		else:
			return sim

def generateFromUser():
	printHelpfullness()
	givenWord = ""
	givenWord = getWord()
	if (givenWord == "\q"):
		print("I'm done :<.")
		return -1
	
	sim = ""
	while (True):
		createdWord = generate(givenWord)
		displayPair(givenWord, createdWord)
		trial = getSim()
		if (trial == '\w'):
			givenWord = getWord()
			if (givenWord == '\q'):
				return -1
		elif (trial == '\q'):
			return -1
		sim = float(trial)
		break
    
	stream = [ [givenWord, createdWord, sim] ]
	while (True):
		createdWord = generate(givenWord)
		displayPair(givenWord, createdWord)
		trial = getSim()
		if (trial == '\w'):
			givenWord = getWord()
			if (givenWord == '\q'):
				print("Thanks! :)")
				break
		elif (trial == '\q'):
			print("Thanks! :)")
			break
		sim = float(trial)
		
		stream += [ [givenWord, createdWord, sim] ]
	return stream
	
		