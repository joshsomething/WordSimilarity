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
import math
from random import random
from getImg import getImg
import sys # For gui stuff.
import atexit # also for gui
# Make a matrix of characters and their filename:
length = 36 #size of matrix

class CharPair:
	def __init__(self, firstChar=None, secondChar=None):
		if (firstChar != None):
			self.firstChar = firstChar
			self.secondChar = secondChar
		else:
			self.firstChar = ""
			self.secondChar = ""
		self.similarity = None
	def getPair(self):
		return [firstChar, secondChar]
	
	def getPics(self, one=None, two=None):
		if (one == None):
			first = getImg("../characters/" + (self.firstChar if self.firstChar != " " else "blank") + ".png")
			second = getImg("../characters/" + (self.secondChar if self.secondChar != " " else "blank") + ".png")
			return list([first, second])
		first = getImg("../characters/" + (one if one != " " else "blank") + ".png")
		second = getImg("../characters/" + (two if two != " " else "blank") + ".png")
		return list([first, second])

	def getDiff(self, one=None, two=None):
		charOne, charTwo = self.getPics(one, two)
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
		attemptPair = [charList[int(random() * 36)], charList[int(random() * 36)]]
		
		#make sure pair is unique, and that the two members of pair are different:
		# TODO: stop recursioning when pairList length equals all the combinations of characters.
		if (attemptPair[0] == attemptPair[1] or (pairList != None and attemptPair in pairList)):
			return CharPair.pickPair(pairList)
		else:
			return attemptPair

	#will return similarity score
	def displayPair(self):
		app = QtGui.QApplication(sys.argv)
		main = CharWindow([self.firstChar, self.secondChar])
		def exithandle():
			print('Similarity: ' + main.similarity)
		atexit.register(exithandle)
		sys.exit(app.exec_())

import time
from PyQt4 import QtGui
from PyQt4.QtCore import *
class CharWindow(QtGui.QMainWindow):
	def __init__(self, pair):
		super(CharWindow, self).__init__()
		self.pair = pair
		self.imageOne, self.imageTwo = self.images()
		self.similarity = ''
		#setGeometry(self, x, y, width, height)
		self.setGeometry(100, 100, 500, 180)
		self.setWindowTitle("Character Similarity scoring.")
		self.info = self.instructions() # 'Friendly' advice telling user about the textbox program.
		self.button = self.enter()
		self.textbox = self.entry() # Box that user will put stuff in.
		self.connect(self.button, SIGNAL("clicked()"), self.getstuff)
		self.show()
	def enter(self):
		btn = QtGui.QPushButton("Enter", self)
		btn.move(300, 42)
		return btn
		
	def instructions(self):
		textbox = QtGui.QLabel(self)
		textbox.resize(220, 40)
		textbox.setText("Please enter the similarity (%):")
		textbox.move(150,0)
		return textbox
		
	def images(self):
		imageLeft = QtGui.QLabel(self)
		imageLeft.resize(100,100)
		imageRight = QtGui.QLabel(self)
		imageRight.resize(100,100)
		imageLeft.setPixmap(QtGui.QPixmap("../characters/" + (self.pair[0] if self.pair[0] != " " else "blank") + ".png"))
		imageRight.setPixmap(QtGui.QPixmap("../characters/" + (self.pair[1] if self.pair[1] != " " else "blank") + ".png"))
		imageLeft.move(0,0)
		imageRight.move(400,0)
		return (imageLeft, imageRight)
		
	def entry(self):
		box = QtGui.QLineEdit(self)
		box.setValidator(QtGui.QDoubleValidator())
		box.setMaxLength(10)
		box.move(200, 2 + self.info.frameRect().height())
		box.setFont(QtGui.QFont("Arial", 20))
		return box

	def getstuff(self):
		self.similarity = self.textbox.text()
		self.close()

	def keyPressEvent(self, event):
		if (event.key() == QtCore.Qt.Key_Return):
			self.similarity = self.textbox.text()
			self.close()

import sys
if (__name__ == '__main__'):
	charOne = charTwo = ''
	if (sys.argv[0] != '—-font'):
		charOne = sys.argv[0]
		charTwo = sys.argv[1]
	CharPair(charOne,charTwo).displayPair()
