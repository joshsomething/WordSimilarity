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

#does the actual predictions, (didn't make the model)

from sklearn.externals import joblib #get the model-loading thing

from sklearn import __version__ as sk_ver
with open("sklearn_version", 'r') as f:
	if (f.read() != sk_ver):
		print("Error: prediction model was made with incompatible version of sklearn_version")
#load model, so that we can make predictions:
mlp = joblib.load('charSim.pkl') #you are my everything.

#extend CharPair class in charPreparer:
from charPreparer.py import CharPair

class CharSim(CharPair):
	def __init__(self, firstChar=None, secondChar=None):
		super(CharPair, self).__init__(firstChar, secondChar)
	#Algorithm, you are now responsible for this,
	#because I'm a lazy human programmer:
	def predict(self, Diff=None):
		if (Diff == None):
			return mlp.predict(super(CharPair, self).getDiff())
		return mlp.predict(super(CharPair, self).getDiff())
	