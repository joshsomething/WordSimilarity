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

from .generator import *
#get user input:
pre_df = generateFromUser()
if (type(pre_df) is int and pre_df < 0):
	print("Come again later (or now), don't quit early")
	sys.exit(-1)

#split up between pairs and similarities:
pairs = [ [pre_df[i][0], pre_df[i][1]] for i in range(len(pre_df))]
similarities = [pre_df[i][2] for i in range(len(pre_df))]

#transform into dictionary:
dataset = {'Pairs': pairs, 'Similarities': similarities}
df = combineData(dataset) #add the data we got to the previous dataset

retrain(df) #use this and re-teach the neural network.
