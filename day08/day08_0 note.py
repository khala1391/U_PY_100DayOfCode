# agenda
# function with input


def greeting():
    print("hello world greeting!")
    print("hello world greeting!")
    print("hello world greeting!")

# greeting()

def greeting_with_name(name):
    print(f"hello {name}")
    print(2+3)

# greeting_with_name("Yut")

# function (parameter)
# parameter = argument

# function more than one input
def greeting_with_alias(a,b):
    print(f"hello {a}, alias is {b}")

# greeting_with_alias("yut","khala")

# def my_function(a, b, c):
    #do this with a
    #then do this with b
    #finally do this with c
# positional argument
# keyword argument
greeting_with_alias(b='khala',a='yut')  #alternative