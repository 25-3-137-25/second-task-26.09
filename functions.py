import math
from decorator import timer, logger

@timer
@logger
def sin(x):
    return math.sin(x)

@timer
@logger
def cos(x):
    return math.cos(x)

@timer
@logger
def exp(x):
    return math.exp(x)

@timer
@logger
def quadratic(x):
    return x*x - 2*x + 1

@timer
@logger
def logistic(x):
    return 1 / (1 + math.exp(-x))
