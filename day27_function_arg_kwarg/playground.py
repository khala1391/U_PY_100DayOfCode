# def add(*arg):
#     for n in arg:
#         print(type(arg))
#         # print(n)

# add(1,2,3,4)


def add(*arg):
    sum = 0
    for n in arg:
        sum += n
    return sum

print(add(1,2,3,4,5,6))


def last(*arg):
    print(arg[-1])

print(last(1,2,3,4,5))

print('-------------------------------------')

def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)
    
calculate(add=2,multiply=3)
print('-------------------------------------')

def cal(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

print('-------------------------------------')

cal(dog=4)
print('-------------------------------------')

def kal(**kwargs):
    print(kwargs["duck"])

kal(dog=2, duck=9)

print('-------------------------------------')

def operate(n ,**kwargs):
    print(kwargs)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(operate(1, add=2,multiply=4))

print('-------------------------------------')


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']
        
        print(f'{self.model}: by {self.make}')
    
    def run(self):
        print('move it move it')
        
my_car = Car(model='top',make='who')
my_car
my_car.run()

print('-------------------------------------')

class Cars:
    def __init__(self, **kwargs:str)-> str:
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        
        print(f'{self.model}: by {self.make}')
        print(f'{self.model}')


new_car =Cars(model='honda')

Cars()