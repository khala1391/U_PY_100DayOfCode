import turtle as turtle_module
import random


# import colorgram

# rgb_colors = []
# colors = colorgram.extract('day18/image.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r,g,b)
    
#     rgb_colors.append(new_color)
    

# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19)]

tim.setheading(225)

for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)







screen = turtle_module.Screen()
screen.exitonclick()