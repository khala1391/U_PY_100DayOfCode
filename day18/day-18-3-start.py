import random
import turtle as t
from turtle import Screen

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    tim.speed(2)
    angle = 360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# for shape in range(3,11):
#     tim.color(random.choice(colours))
#     # tim.color(colours[shape])
#     draw_shape(shape)

for shape in range(3,len(colours)+3):
    # tim.color(random.choice(colours))
    index = shape - 3
    tim.color(colours[index])
    draw_shape(shape)

tim.screen.mainloop()  # always show screen

