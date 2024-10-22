# datatype
# [] refer to position of data
# [] is subscripting

# print("hello"[0])
# print("hello"[4])
#
# w = input("add word")
# print(len(w))

# string
print("123" + "456")

# integer
print(123 + 456)

# symbol for comma > python skip this
print(123_456)

# float (floating point number)
print(3.14159)

# boolean
# true or false

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# len function work for string data
# len(123) >> error

# num_char = len(input("what is your name?\n"))
# print(num_char)
# print(type(num_char))
#
# new_num_char = str(num_char)
# # result
# # <class 'int'>
#
# # print("your name has"+ num_char + "characters.") >> not work
# print("your name has "+ new_num_char + " characters.")
# print(f"your name has  {num_char}  characters.")

print(float(100.5))
print(70+float(100.5))
print(str(70)+str(100))


# math operator
# divide always get float datatype

a = 3+5
b = 4-2
c = 6*1
d = 2/4
e = 6/3
f = 2**3

print(a, b, c, d, e, f)
print(type(d))
print(type(f))

# PEMDUS
# parentheses  ()
# exponents **
# multiplication *
# division /
# addition +
# subtraction -

# #quotient
# print(9//2)
# print(19//2)
# print(type(19//2))

# mod
# print(14%3)
# print(74%7)
# print(type(74%7))

# abbrev form mostly use in for i +=, -=, *=, /=
result1 = 16/2

# full form: result1 = result1/2
# result1 = result1/2
result1 /= 2
print(result1)

result2 = 4+7
result2 += 3
print(result2)
# true <> True
bool = True
print(type(bool))

# f string
print(f"result1 is {result1} and result2 is {result2} and {bool}")

print(round(2.58888,2))

