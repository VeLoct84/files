import numpy as np
import draw

print("Please select the size of canvas?")
print("a - 800 x 600\n
      b - 400 x 300\n
      c - 1000 x 800")

#canvas = draw.Canvas(width=600, height=800, color=(255, 255, 255))
#
## loop random shape
#for r in range(10):
#    width_random = np.random.randint(canvas.width / 2)
#    height_random = np.random.randint(canvas.height / 2)
#    side_random = np.random.randint(200)
#
#    # create shape rectangle.
#    r1 = draw.Rectangle(
#        x=width_random,
#        y=height_random,
#        width=width_random,
#        height=height_random,
#        color=canvas.rgb_regenerator(),
#    )
#    r1.draw(canvas)
#
#    # create shape square.
#    s1 = draw.Square(
#        x=width_random,
#        y=height_random,
#        side=side_random,
#        color=canvas.rgb_regenerator(),
#    )
#    s1.draw(canvas)
#
#canvas.make(imagepath="canvas.png")
