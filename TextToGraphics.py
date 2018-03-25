# Turns text into image:
from PIL import Image, ImageDraw, ImageFont
import sys
text = sys.argv[len(sys.argv) - 1]
image = Image.new('L', (100, 100), 255) # Create blank 'canvas'

draw = ImageDraw.Draw(image) # Drawing object
font = ImageFont.truetype("/usr/share/fonts/truetype/arkpandora/Aerial.ttf", size=25)
draw.text((50, 50), text, 0, font=font)

image.save(text + ".png", "PNG")
