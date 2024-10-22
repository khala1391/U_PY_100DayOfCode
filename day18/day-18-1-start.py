#####Turtle Intro######

import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

# from turtle import Turtle
#
# tim = Turtle()  # create object 'tim' from Turtle Class
# tom = Turtle()
# terry = Turtle()

# not good
# from turtle import *  # difficult to identify source
# from random import * # ok

# import turtle as t
# tim = t.Turtle()

# import heroes
# print(heroes.gen())

######## Challenge 1 - Draw a Square ############

timmy = t.Turtle()

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
