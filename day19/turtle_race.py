import turtle
from turtle import Turtle, Screen
import random

factor = 1
width_set = 500*factor
height_set = 400*factor

screen = Screen()
screen.setup(width=width_set, height=height_set)
width_edge = (screen.window_width())/2
height_edge = (screen.window_height())/2

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
num_turtle = len(colors)

colors_concat = ", ".join(colors)

print(colors_concat)

user_guess = screen.textinput(title="turtle race",prompt=f"guess winner:\n({colors_concat}) ")

def move_forwards():
    new_turtle.forward(10)

all_turtles = []


# print(user_guess)
for i in range(num_turtle):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-width_edge + 20, y=-height_edge + 30 * factor + i * height_set / num_turtle)
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > width_edge-30:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_guess:
                print(f"You've won(guess: {user_guess})!!! The winner is {winning_color}")
            else:
                print(f"You've lost(guess: {user_guess}) !!! The winner is {winning_color}")

        i.forward(random.randint(1,20))

screen.exitonclick()