import math
from decorator import *

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
@no_zero_division
def obr_proporc(x):
    return 1 / x
