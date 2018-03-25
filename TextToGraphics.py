'''     Copyright 2018 Joshua Danielpour


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

# Turns text into image:
from PIL import Image, ImageDraw, ImageFont
import sys
text = sys.argv[len(sys.argv) - 1]
image = Image.new('L', (100, 100), 255) # Create blank 'canvas'

draw = ImageDraw.Draw(image) # Drawing object
font = ImageFont.truetype("/usr/share/fonts/truetype/arkpandora/Aerial.ttf", size=25)
draw.text((50, 50), text, 0, font=font)

image.save("characters/" + text + ".png", "PNG")
