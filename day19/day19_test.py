# https://youtu.be/FJ7iT-0XFQk?si=KhDEv4siI7mWudQH
def beta(a: str, b: int, c):  # just hint, not static
    print(a.upper())
    print(c)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(n1=6, n2=3, func=add)
#use key argument (instead of positional argument)
print(result)
