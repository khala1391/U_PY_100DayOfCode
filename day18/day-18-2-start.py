import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

from turtle import Turtle, Screen
tt_turtle_obj = Turtle()

for _ in range(15):
    tt_turtle_obj.forward(10)
    tt_turtle_obj.penup()
    tt_turtle_obj.forward(10)
    tt_turtle_obj.pendown()

screen = Screen()
screen.exitonclick()
