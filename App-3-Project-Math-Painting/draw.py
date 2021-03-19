import numpy as np
from PIL import Image


class Canvas:
    """
    Create instant object to create background of a canvas

    Param width= provide int or float
    Param height= provide int or float
    Param color= in Red, Blue, Green 'RGB'
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # generate array zeroes from numpy
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color

    # RGB random colour
    def rgb_regenerator(self):
        rgb = []
        for x in range(3):
            sequence = np.random.randint(255)
            rgb.append(sequence)
        return rgb

    # to create images for canvas
    def make(self, imagepath):
        """
        Parameter imagepath: to save canvas in path that provided
        """
        canvas = Image.fromarray(self.data, mode="RGB")
        canvas.save(imagepath)
