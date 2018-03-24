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
# translates pictures to the center of the frame:
# NOTES:
#  - This will not work for characters that have white vertical gaps in them.
#  - Currently, this has been setup so that all images have to have the same height and width.

import numpy as np
import cv2
from PIL import Image

# cv2.imread() doesn't sem to work correctly (at least on my system)
# using pillow instead.
def getImg(file):
	pil_image = Image.open(file).convert('RGB')
	cv_img = np.array(pil_image)
	#turn RGB to BGR:
	print(cv_img)
	return cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY) # Convert to grayscale (makes life easier).


#The height of the images seem to be different for each system.
picHeight, picWidth = getImg("a.png").shape

#opencv layout (row, column): (0,0) is top-left
#grayscale: 255 is white, 0 is black
#starts from left, finds the rightmost column of an object (indicated by blackness)
def findRight(image): #scan each column from top to bottom:
	mostRight = 0
	fromBlackCol = False # Make sure  don't quit when starting on white column.
	for col in range(picWidth):
		for row in range(picHeight):
			#we'll say that everything that's more than 180 is too white:
			if (image.item(row, col) <= 180):
				# We'll increment mostRight, go to the next column,
				# and flag that we've reached a black-pixel-containing column
				# when we get contact with a black pixel:
				fromBlackCo = True
				mostRight += 1
				break
		#if no black(ish) pixel is in the current column, then stop searching:
		if (fromBlackCol == True and mostRight - 1 != col):
			return mostRight

def findLeft(image): #scan each column from top to bottom:
	for col in range(picWidth):
		for row in range(picHeight):
			if (image.item(row, col) <= 180):
				print(image.item(row, col))
				return col # stop when we've found a black-containing column.
	return picWidth - 1

def findTop(image):
	#from top to bottom, scan each row from left to right
	#stop when we find a black pixel:
	mostUp = 0
	fromBlackRow = False #Make sure we don't stop when starting on a white column.
	for row in range(picHeight):
		for col in range(picWidth):
			if (image.item(row, col) <= 180):
				fromBlackRow=True
				break
		# If no black was found on current row,
		# increase the row number by one.
		mostUp += 1

		if (fromBlackRow==True and mostUp - 1 != col):
			return mostUp

def findBottom(image):
	# From bottom to top, scan each row from left to right.
	# Stop when we find a black pixel:
	mostDown = picHeight - 1
	fromBlackRow = False
	for row in reversed(range(picHeight)):
		for col in range(picWidth):
			if (image.item(row, col) <= 180):
				fromBlackRow = True
				break

			mostDown -= 1
		if (fromBlackRow==True and mostDown + 1 != col):
			return mostDown

def getCenter(image):
	leftSide = findLeft(image)
	rightSide = findRight(image)
	topSide = findTop(image)
	bottomSide = findBottom(image)
	
	#distance from left side to right side:
	length = rightSide - leftSide

	#distance from top to bottom:
	height = bottomSide - topSide
	
	#x, y
	return [int(length * .5), int(topSide + height * .5)]
	


#move object to the center of the image (picWidth/2, picHeight/2):
def centerObject(image): #positive: right, down
	#some of this function (centerObject) was inspired from 
	#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#translation
	
	frameCenter = [int(picWidth/2), int(picHeight/2)]
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
image = getImg(character + ".png")

#center the image:
centeredImage = centerObject(image)

#write the centeredImage to file:
cv2.imwrite(character + ".png", centeredImage)
