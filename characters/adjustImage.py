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
# translates pictures to the center of the frame:

import numpy as np
import cv2

#opencv layout (row, column): (0,0) is top-left
#grayscale: 255 is white, 0 is black
def findRight(image): #scan each column from top to bottom:
	mostRight = 0
	for col in range(56):
		for row in range(50):
			#we'll say that everything that's more than 180 is too white:
			if (image[row][col] <= 180):
				#we'll increment mostRight, and go to the next column
				#when we get contact with a black pixel:
				mostRight++
				break
		#if no black(ish) pixel is in the current column, then stop searching:
		if (mostRight - 1 != col):
			return mostRight

def findTop(image):
	#from top to bottom, scan each row from left to right
	#stop when we find a black pixel:
	mostUp = 0
	for row in range(50):
		for col in range(56):
			if (image[row][col] <= 180):
				break
			mostUp++
		if (mostUp - 1 != col):
			return mostUp

def findBottom(image):
	#from bottom to top, scan each row from left to right
	#stop when we find a black pixel:
	mostDown = 55
	for row in range(50):
		for col in reversed(range(56)):
			if (image[row][col] <= 180):
				break
			mostDown--
		if (mostDown + 1 != col):
			return mostDown

def getCenter(image):
	leftSide = 0
	rightSide = findRight(image)
	topSide = findTop(image)
	bottomSide = findBottom(image)
	
	#distance from left side to right side:
	length = rightSide
	
	#distance from top to bottom:
	height = bottomSide - topSide
	
	#x, y
	return [length * .5, topSide + height * .5]
	


#move object to the center of the image (25, 28):
def centerObject(image): #positive: right, down
	#some of this function (centerObject) was inspired from 
	#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#translation
	
	frameCenter = [25, 28]
	#if image center is : [24, 28], 25 - 24 : move image right by one
	#if image center is : [25, 27], 28 - 27 : move image down by one
	pictureCenter = getCenter(image)
	rows, cols = image.shape
	right = frameCenter[0] - pictureCenter[0]
	down = frameCenter[1] - pictureCenter[1]
	
	#transform: np.float32([[1, 0, right], [0, 1, down]])
	M = np.float32([[1,0,right],[0,1,down]])
	return cv2.warpAffine(image,M,(cols,rows))
#get character from arguments:
import sys

if (len(sys.argv) < 2):
	raise("Error: please enter a character")

character = sys.argv[1]

#get image from character:
image = cv2.imread(character + ".png", 0)
#center the image:
centeredImage = centerObject(image)

#write the centeredImage to file:
cv2.imwrite(character + ".png", centeredImage)

	