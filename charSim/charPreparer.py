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

#prepares characters to be evaluated:

# load character list
charList = [] #character list
for letter in range(97, 123):
	charList.append(chr(letter))

for digit in range(10):
	charList.append(chr(digit + ord('0')))

import numpy as np
import cv2 #for images.
import math #for rand
from .getImg import getImg
#make a matrix of characters and their filename:
length = 36 #size of matrix

class CharPair:
	def __init__(self, firstChar=None, secondChar=None):
		if (firstChar != None):
			self.firstChar = firstChar
			self.secondChar = secondChar
		else:
			self.firstChar = ""
			self.secondChar = ""
	def getPair(self):
		return [firstChar, secondChar]
	
	def getPics(self, one=None, two=None):
		if (one == None):
			return [getImg("../characters/" + (self.firstChar if self.firstChar != " " else "blank") + ".png")
				, getImg("../characters/" + (self.secondChar if self.secondChar != " " else "blank") + ".png")]
		return [getImg("../characters/" + (one if one != " " else "blank") + ".png")
			, getImg("../characters/" + (two if two != " " else "blank") + ".png")]
		
	def getDiff(self, one=None, two=None):
		charOne, charTwo = getPics(one, two)
		
		diff = [[0 for x in range(len(charOne[0]))] for y in range(len(charOne))]
		for x in range(len(charOne)):
			for y in range(len(charTwo)):
				#it's okay that we can get negative values.
				diff[x][y] = charOne[x][y] - charTwo[x][y]
		
		return diff
	
	def setPair(self, one, two):
		self.firstChar = one
		self.secondChar = two
		
	
	#pick pair, if specified, will make sure pair is unique
	def pickPair(pairList=None):
		#try to get pair:
		attemptPair = [charList[int(math.random() * 37 )], charList[int(math.random() * 37 )]]
		
		#make sure pair is unique, and that the two members of pair are different:
		if (attemptPair[0] == attemptPair[1] or (pairList != None and attemptPair in pairList)):
			return pickPair(pairList)
	
	import sys
	
	#will return similarity score
	def displayPair():
		app = QtGui.QApplication(sys.argv)
		
		return CharWindow([self.charOne, self.charTwo]).similarity
		
    	
from PyQt4 import QtGui
from PyQt4.QtCore import *
class CharWindow(QtGui.QMainWindow):
	def __init__(self, pair):
		super(Window, self).__init__()
		self.pair = pair
		self.images()
		self.similarity = 0.0
		self.setGeometry(100, 100, 600, 600)
		self.setWindowTitle("Character Similarity scoring.")
		self.entry()
		self.instructions()
		self.enter()
		
		self.show()
	def enter(self):
		btn = QtGui.QPushButton("Enter", self)
		btn.move(500, 300)
		
	def instructions(self):
		textbox = QtGui.QLabel()
		textbox.setText("Please enter the similarity (%):")
		textbox.setAlignment(Qt.AlignCenter)
		
	def images(self):
		imageLeft = QLabel(self)
		imageRight = QLabel(self)
		imageLeft.setPixmap(QPixmap("../characters/" + (self.pair[0] if self.pair[0] != " " else "blank") + ".png"))
		imageRight.setPixmap(QPixmap("../characters/" + (self.pair[1] if self.pair[1] != " " else "blank") + ".png"))
		imageLeft.setAlignment(Qt.AlignLeft)
		imageRight.setAlignment(Qt.AlignRight)
		
	def entry(self):
		box = QLineEdit(self)
		box.setValidator(QDoubleValidator())
		box.setMaxLength(10)
		box.setAlignment(Qt.AlignCenter)
		box.setFont(QFont("Arial", 20))
		box.connect(self.enter, SIGNAL("clicked()"), self.getstuff)
		
	def getstuff(self, value):
		self.similarity = value
		self.close()


