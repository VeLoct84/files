import numpy as np
from PIL import Image
from random import randint

data = np.zeros((10, 10)),
data[:] = [255, 128, 0]

# add green colour patch
#data[1:3] = [0,255,0]

image = Image.fromarray(data, mode='RGB')
image.save('canvas.png')
