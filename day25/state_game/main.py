import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# get coordinate on screen
# *******************************
# def get_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_coor)
# *******************************

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        
        # print(missing_state)
        
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        # t.write(state_data.state.item())
        t.write(answer_state)
        guessed_states.append(answer_state)
























# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)

 
# screen.mainloop()
# turtle.mainloop()
