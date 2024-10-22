# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def turn_around():
#     turn_left()
#     turn_left()
#
# def move_circle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_around()
#
# move_circle()
# move_circle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def zigzag():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

#
# for i in range(6):
#     zigzag()

# zigzag()
# zigzag()
# zigzag()
# zigzag()
# zigzag()
# zigzag()

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     zigzag()
#     number_of_hurdles -= 1

# number_of_hurdles = 6
# while at_goal() == False :
#     zigzag()
#     number_of_hurdles -= 1

# while at_goal() == False :
#     zigzag()

# while at_goal() != True :
#     zigzag()
# while not at_goal():
#     zigzag()

# for loop: better for specific
# while loop: better for case do not care about number of loop
    # may run forever (infinite loop)
# while 5>3:
    # do this

# hurdle#3
# def zigzag_new():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() != True :
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         zigzag_new()
# way#2
# while at_goal() != True:
#     if wall_in_front():
#         zigzag_new()
#     else:
#         move()

# hurdle#4
# def turn_hurdle():
#     turn_right()
#     move()
#     turn_right()
#     move()
#
# while at_goal() != True :
#     if wall_in_front() == False and wall_on_right():
#         move()
#     elif wall_in_front() == True and wall_on_right():
#         turn_left()
#     else:
#         turn_hurdle()

# Maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# for prevent infinite loops
# while front_is_clear():
#     move()
# turn_left()
#
# while at_goal() != True:
#     if not wall_on_right():
#         turn_right()
#         move()
#     elif wall_in_front() == True and wall_on_right() == True:
#         turn_left()
#     else:
#         move()

