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

from wordPreparer.py import UnevenWordPair
import sklearn
import numpy as np

import sys
if ("--create-df" in sys.argv):
	UnevenWordPair.createDF()
import pandas as pd

#select dataset (change if you want to use a different named dataset (probably not)):
df = pd.read_csv('wordsim.csv')

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
#create our model:
mlp = MLPRegressor(hidden_layer_sizes=(100, 100, 500), warm_start=True) #make 3 hidden layers with 
#100, 100 and 500 nodes, respectively

#do your work, complicated math!
mlp.fit(X_train, y_train) # :D

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
f = open('wordSimCalc.out', 'ab') #append mode

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
joblib.dump(mlp, 'wordsim.pkl')