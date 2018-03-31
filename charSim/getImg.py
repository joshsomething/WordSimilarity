from PIL import Image

import numpy as np

def getImg(file):
	return np.array(Image.open(file))
