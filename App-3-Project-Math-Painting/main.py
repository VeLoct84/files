import numpy as np
import draw
from shape import Rectangle, Square

# optional selected canvas size by user
size_canvas = {
    "a": [1024, 768],
    "b": [800, 600],
    "c": [320, 240]
    }


# color for background canvas
background_canvas ={
    "a" : (255, 255, 255),
    "b" : (0, 0, 0),
    "c" : (128, 128, 128)
    }

while True:
    # ask user to do selection to set canvas
    print("Please select the size of canvas?")
    print("a - 1024 x 768\nb - 800 x 600\nc - 320 x 240\nd - custom")
    select = input(">>> ")

    for selection in size_canvas.keys():
        if select.lower() == selection:
            # ask user for background color
            print("Background color for canvas?")
            print("a - White\nb - Black\nc - Grey")
            background = input(">>> ")

            canvas = draw.Canvas(
                width=size_canvas[select][0], 
                height=size_canvas[select][1], 
                color=background_canvas[background]
                )

    if select.lower() == "d":
        # this conditional for selection 'd'
        canvas_width = int(input("Enter width size: "))
        canvas_height = int(input("Enter height size: "))

        # ask user for background color
        print("Background color for canvas?")
        print("a - White\nb - Black\nc - Grey")
        background = input(">>> ")
        
        canvas = draw.Canvas(
            width=canvas_width,
            height=canvas_height,
            color=background_canvas[background]
            )

    # to ask user to run random shape to paint
    print("Do you want generate random abstrack painting? [y/n]")
    user_selection = input(">>> ")

    if user_selection.lower() == "y":
        # loop random shape
        for r in range(10):
            width_random = np.random.randint(canvas.width / 2)
            height_random = np.random.randint(canvas.height / 2)
            side_random = np.random.randint(200)

            # create shape rectangle.
            r1 = Rectangle(
                x=width_random,
                y=height_random,
                width=width_random,
                height=height_random,
                color=canvas.rgb_regenerator(),
            )
            r1.draw(canvas)

            # create shape square.
            s1 = Square(
                x=width_random,
                y=height_random,
                side=side_random,
                color=canvas.rgb_regenerator(),
            )
            s1.draw(canvas)
    # save the path
    canvas.make(imagepath="canvas.png")
    print(f"The canvas.png has been save")
    break

    if user_selection.lower() == "n":
        break

