# list of number
# numbers = [1,2,3]
# new_numbers = [i+1 for i in numbers]
# new_numbers

# list of string
# name = "Angela"
# letter_list = [letter for letter in name]
# letter_list

# list of number
new_list = [n*2 for n in range(1,5)]
new_list

def rectangle(w,h):
    """_summary_

    Args:
        w (_type_): _description_
        h (_type_): _description_

    Returns:
        _type_: _description_
    """
    return w*h
import math

def circle(r:float) -> float:
    """_summary_

    Args:
        r (float): _description_

    Returns:
        float: _description_
    """
    return math.pi * r * r

circle(1)
circle()