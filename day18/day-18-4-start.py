import turtle as t
import random
t.colormode(255)
tim = t.Turtle()        # create object 'tim' from 'Turtle' Class

# color_name
# https://cs111.wellesley.edu/reference/colors

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
def rand_col():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    col_rgb = (r, g, b)     # tuple
    return col_rgb




direction = [0, 90, 180, 270]
tim.pensize(10)

for _ in range(100):
    # tim.pencolor(random.choice(colours))
    tim.color(rand_col())
    tim.forward(30)
    tim.setheading(random.choice(direction))

# turtle.setheading(90)  # set
# turtle.heading()  # call current setting