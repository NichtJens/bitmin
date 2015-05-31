
from math import log, ceil


def next_heigher_power_of_2(number):
    '''
    calculate n such that 2**n >= number > 2**(n-1)
    '''
    return int(ceil(log(number) / log(2)))

