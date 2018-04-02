'''	 Copyright 2018 Joshua Danielpour


	This file is part of WordSimilarity.

    WordSimilarity is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    WordSimilarity is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with WordSimilarity.  If not, see <http://www.gnu.org/licenses/>.
'''

#[ [similarities at each index], [similarities (first -> second + 1)],
#"abc", "bac" : sim: [a-a, b-c, c-c], sim: []
import sklearn
import numpy as np
from ../charSim/_charSim import CharSim
import pandas as pd

class WordPair(CharSim):
	def __init__(self, wordOne=None, wordTwo=None):
		if (wordOne != None):
			self.wordOne = wordOne
			self.wordTwo = wordTwo
	def getDiffs(self)
		return [super(WordPair, self).getDiff(self.wordOne[i], self.wordTwo[i]) for i in range(len(self.wordOne))]
	def getCrossDiffs(self):
		return [
			[super(WordPair, self).getDiff(self.wordOne[i], self.wordTwo[(i + 1) % len(self.wordTwo)] for i in range(len(self.wordOne))]
			, [super(WordPair, self).getDiff(self.wordOne[(i + 1) % len(self.wordOne)], self.wordTwo[i] for i in range(len(self.wordOne))]
			]
	def getImages(self):
		return [super(WordPair, self).getPics(self.wordOne[i], self.wordTwo[i]) for i in range(len(self.wordOne))]
	
	def getPairs(self):
		return [super(WordPair, self).__init__(self.wordOne[i], self.wordTwo[i]) for i in range(len(self.wordOne))]
	def getWordPair(self):
		return [self.wordOne, self.wordTwo]
	def getSims(self, diffList=None):
		if (diffList == None):
			return [self.getPairs()[i].predict() for i in range(len(self.wordOne))]
		return [CharPair().predict(diffList[i]) for i in range(len(self.wordOne))]
	def createDF(self, wordFile="words", simFile="sims", out="wordsim.csv"):
		wordy = open(wordFile, "r")
		
		line = wordy.readline()
		words = [ [line[:line.find(", ")], line[line.find(", ") + 2:]] ]
		while (True):
			line = wordy.readline()
			if (line == ""):
				break
			words += [line[:line.find(", ")], line[line.find(", ") + 2:]]
		wordy.close()
		
		simy = open(sims, "r")
		
		line = simy.readline()
		sims = [float(line)]
		while (True):
			line = simy.readline()
			if (line == ""):
				break
			sims += [float(line)]
		simy.close()
		
		dataset = {"Pairs": words, "Similarities": sims}
		df = pd.DataFrame(dataset, columns=['Pairs', 'Similarities'])
		
		df.tocsv(out)
	def meanSim(self):
		return sum(self.getSims())/len(wordOne)


#if words don't have the same length, put blanks at the end:
def padWords(wordOne, wordTwo):
	rWords = [wordOne, wordTwo]
	while(len(rWords[0]) < len(rWords[1])):
		rWords[0] += " "
	while(len(rWords[1]) < len(rWords[0])):
		rWords[1] += " "
	return rWords
	
import time
#rearrange blanks so that mean similarity is higher:
def kindlyPadWords(wordOne, wordTwo, timeLimit = 15, reductionTime = 3):
	numBlanks = abs(len(wordOne) - len(wordTwo))
	if (numBlanks == 0):
		return [wordOne, wordTwo]
	firstLess = len(wordOne) < len(wordTwo)
	#blank limit: how much blanks can be arranged in a group before it's too much 
	#to make it easier for myself, I'll just say 35% of the larger word.
	blankLimit = int(.35 * max(len(wordOne), len(wordTwo)))
	#the mean similarity we'd have if we just put the blanks at the end
	one, two = padWords(wordOne, wordTwo)
	startingPoint = WordPair(one, two).meanSim()
	current = startingPoint
	
	timestart = time.time()
	if (firstLess):
		previous = ""
		timeLoop = time.time()
		for pos in range(len(one)):
			if (numBlanks == 0 or blankLimit == 0 or time.time() - timestart > timeLimit):
				return [one, two]
			elif (time.time() - timeLoop > reductionTime):
				blankLimit -= 1 #reducing this reduces the combinations required, thus reducing the time for this function to finish
				reductionTime += 1
				timeLoop = time.time()
				
			placed = 0
			for place in range(1, (blankLimit if blankLimit <= numBlanks else numBlanks) + 1):
				placement = WordPair( (previous + (" " * place) + wordOne[pos:] + (" " * (numBlanks - place))), wordTwo)
				if (placement.meanSim() > current):
					current = placement.meanSim()
					one, two = placement.getWordPair()
					placed = place
				if (place == (blankLimit if blankLimit <= numBlanks else numBlanks)):
					previous += placement.getWordPair[0][pos + place:pos + place + 1]
			previous += " " * placed
			numBlanks -= placed
			placed = 0
			
	else:
		previous = ""
		timeLoop = time.time()
		for pos in range(len(one)):
			if (numBlanks == 0 or blankLimit == 0 or time.time() - timestart > timeLimit):
				return [one, two]
			elif (time.time() - timeLoop > reductionTime):
				blankLimit -= 1
				reductionTime += 1
				timeLoop = time.time()
			
			placed = 0
			for place in range(1, (blankLimit if blankLimit <= numBlanks else numBlanks) + 1):
				placement = WordPair( wordOne, (previous + (" " * place) + wordTwo[pos:] + (" " * (numBlanks - place))))
				if (placement.meanSim() > current):
					current = placement.meanSim()
					one, two = placement.getWordPair()
					placed = place
				if (place == (blankLimit if blankLimit <= numBlanks else numBlanks)):
					previous += placement.getWordPair[1][pos + place:pos + place + 1]
			previous += " " * placed
			numBlanks -= placed
			placed = 0
	return [one, two]
	
class UnevenWordPair(WordPair):
	def __init__(self, wordOne, wordTwo):
		paddedOne, paddedTwo = padWords(wordOne, wordTwo)
		
		self.rawPair = super(UnevenWordPair, self).__init__(paddedOne, paddedTwo)
		self.rearrangedPair = kindlyPadWords(wordOne, wordTwo)
	def rearranged(self):
		one, two = self.rearrangedPair
		return WordPair(one, two)
	
	def getRaw(self):
		return self.rawPair

	def getFinalArrangement(self):
		rawlyPadded = self.rawPair
		nicelyPadded = WordPair(self.rearrangedPair)
		
		diffArrangement = [ 
			([self.rawPair.getDiffs()] + [self.rawPair.getCrossDiffs()]),
			([nicelyPadded.getDiffs()] + [nicelyPadded.getCrossDiffs()])
			]
		
		finalSims = [[CharPair().getSims(diffArrangement[0][i]) for i in range(3)]]
		finalSims += [[CharPair().getSims(diffArrangement[1][i]) for i in range(3)]]
		
		return finalSims
