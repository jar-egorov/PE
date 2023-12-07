import math

def x():
    return int(input()) ** 2 + 3
def y():
    return math.sin(4)
def f(x, y):
    return x() + y()

print(f(x, y))