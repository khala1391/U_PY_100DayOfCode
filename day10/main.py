def power(a,b):
    return a**b

result = power(2,3)
power(3,1)

print(result)

# ----------------------------------------------------

text = "they're bill's friends from the UK"

print(text.title())

# ----------------------------------------------------

text = 'pascal case example'
''.join(x for x in text.title() if not x.isspace())

# ----------------------------------------------------
def tname(f_name):
    name = f_name.title()
    return print(f'result is {name}')

tname("oreo")

# ----------------------------------------------------

def echo(text):
    return (text +" "+ text).title()

echo("hello")
print(echo("hello"))

# ----------------------------------------------------

def add(a, b):
    """
    add number\n
    add number\n
    add number\n
    add number\n
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        return "exit"
    return a + b

add(2,3)

def add2(a, b):
    """add number 
    add number 
    add number 
    add number
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        return "exit"
    return a + b

add(2,3)
add2
