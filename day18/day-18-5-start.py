import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
tim.pensize(0.5)
tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.circle(80)
#     tim.left(5)

def draw_circle_num(num_circle):
    for _ in range(num_circle):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading()+360/num_circle)

def draw_circle_gap(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading()+gap)

draw_circle_num(80)
# draw_circle_gap(4)


screen = Screen()
screen.exitonclick()