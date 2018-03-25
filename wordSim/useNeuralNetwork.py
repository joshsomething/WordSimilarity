'''	Copyright 2018 Joshua Danielpour


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


from .wordPreparer import * #feelin' lazy.
from .generator import *
import sys
modelFile = ""
if ("--use-tuned" in sys.argv or "-t" in sys.argv):
	modelFile = "tunedwordsim.pkl"
elif ("--custom" in sys.argv):
	modelFile = sys.argv[sys.argv.index("--custom") + 1]
else:
	modelFile = "wordsim.pkl"

from sklearn.externals import joblib
model = joblib.load(modelFile)

index = 0
print("Just go along with the ride, press '\q' to quite!")
while (True):
	print ("Pair #" + index + ":")
	print("")
	
	wordOne = getWord(message="Enter a word: ")
	if (wordOne == '\q'):
		break
	
	wordTwo = getWord(message="Enter another one: "):
	if (wordTwo == '\q'):
		break
	print("The similarity is: " + model.predict(UnevenWordPair(wordOne, wordTwo).getFinalArrangement()))

print("Hope you enjoyed!")
print(":-)")

