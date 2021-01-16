import math

def add(*args):
    for i in args:
        assert type(i) == int , "please enter an integer"

    num = list(args)
    return sum(num)

def multiply(*args):
    for i in args:
        assert type(i) == int , "please enter an integer"

    num = list(args)
    res = math.prod(num)
    return res
    

print(add(1, 2, 3, 4))
print(multiply(1,2,3, 4))