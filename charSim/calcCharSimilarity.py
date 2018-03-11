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

#Uses the actual neural networks and whatnot to find similarity between
#characters.

#get the libraries we need:
import numpy as np
import math
import sklearn as skl

#use the class defined in charSim.py:
from charPreparer.py import CharPair #use this to get user input and whatnot

#data layout: pairs of data, difference, similarity
	#pairs of data: name (letter/number) and picture (we don't have to worry about this part)


#choose pairs, I'll do 60 in total:
pairs = [CharPair.pickPair()]

#add more pairs, again up to 60:
for pairy in range(1, 60):
	pairs.append(CharPair.pickPair(pairs))

#add difference and similarity into the picture (no pun intended ... or is it):
differences = CharPair(pairs[0]).getDiff()
similarities = CharPair(pairs[0]).displayPair()
for i in range(1, 60):
	currentPair = CharPair(pairs[i])
	differences.append(currentPair.getDiff())
	similarities.append(currentPair.displayPair())

from pandas import pd
#make dataset:
dataset = {'Pairs': pairs, 'Differences': differences, 'Similarities': similarities}
df = pd.DataFrame(dataset, columns=['Pairs', 'Differences', 'Similarities'])

#export just to keep hard-earned work safe:
from datetime import date
#ensure we don't destroy previous work:
timestamp = str(datetime.datetime.today()).replace(' ', '_') 
df.to_csv('character_data_' + timestamp + ".csv") # ;)



#x scale : difference:
x = df.loc['Differences']

#y scale : similarity:
y = df.loc['Similarities']


#split half the data for the algorithm to learn from,
#half to test the results later:
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5)


#for the moment of truth, now for the actual learning!
from sklearn.neural_network import MLPRegressor
#create our model:
mlp = MLPRegressor(hidden_layer_sizes=(100, 100, 500)) #make 3 hidden layers with 
#100, 100 and 500 nodes, respectively

#do your work, complicated math!
mlp.fit(x_train, y_train) # :D

#evaluate the results:
#get the predictions out of the testing data:
y_predicted = mlp.predict(x_test)

#get the average error:
from sklearn.metrics import mean_absolute_error 
absErr = mean_absolute_error(y_test, y_pred)
debug = ["Error rate (mean): " + str(absErr),
"Predicted y values: " + "[" + ", ".join( str(x) for x in y_predicted) + "]",
"Real y values: " + "[" + ", ".join( str(x) for x in y_test) + "]",
"Predicted y values: " + "[" + ", ".join( str(x) for x in y_predicted) + "]"]

#open file to save the scoring:
f = open('calcCharSimilarity.out', 'ab') #append mode

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
joblib.dump(mlp, 'charSim.pkl')