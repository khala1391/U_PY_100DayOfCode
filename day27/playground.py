def add(*args):
#    print(args)
#    print(type(args))
    sum = 0
    for n in args:
        sum += n
    return sum
        

print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))


tuple =(10,11,12,13)
print(tuple[3])
# ---------------------------------------------------- 


def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for k, v in kwargs.items():
        # print(k)
        # print(v)

    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)
    

calculate(4, add=3, multiply=5)

# ---------------------------------------------------- 
scores = {
    'Physics': 67, 
    'Maths': 87,
    'History': 75
}

result = scores.get('Physics')

print(result)    # 67
# ---------------------------------------------------- 
def add(n):
    return n+n

def pow(n):
    return n**n


def operate(n, **kwargs):
    func = kwargs.get('func')
    if func is not None:
        return func(n)

operate(3, func=add)
operate(3, func=pow)


# ---------------------------------------------------- 

class Car:
    
    def __init__(self,**kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']   # return error, if missing
        self.year = 2005
        self.country = kwargs.get("country")   # return None, if not input
        
# my_car = Car()
my_car = Car(make="Nissan", model= "GT-R")
print(my_car.model)
print(my_car.year)
print(my_car.country)


# ---------------------------------------------------- 

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)