class Square:
    """
    Creating shape square.

    param x= coordination for x-axis
    param y= coordination for y-axis
    param side= width and height length square
    param color= required 3 argument for mode RGB
    """

    def __init__(self, x, y, side, color):

        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """
        param canvas : input from parents class canvas
        """
        canvas.data[
            self.x : self.x + self.side, self.y : self.y + self.side
        ] = self.color


class Rectangle:
    """
    Class return rectangle shape

    param x= coordination for x-axis
    param y= coordination for y-axis
    param width= width length for rectangle
    param height= height length for rectangle
    param color= required 3 argument for mode RGB
    """

    def __init__(self, x, y, width, height, color):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """
        param canvas : input from parents class canvas
        """
        canvas.data[
            self.x : self.x + self.width, self.y : self.y + self.height
        ] = self.color
