
from mathhelper import next_heigher_power_of_2



def bm2i(bitmask, min_i=0, max_i=None):
    '''
    convert a bitmask to an index list
    '''
    if max_i is None:
        max_i = next_heigher_power_of_2(bitmask)

    return [i for i in xrange(min_i, max_i) if (bitmask & (1<<i))]


def i2bm(indices):
    '''
    convert an index list to a bitmask
    '''
    return sum([1<<i for i in indices])



def bm2bl(bitmask, min_i=0, max_i=None):
    '''
    convert a bitmask to a list of booleans
    '''
    if max_i is None:
        max_i = next_heigher_power_of_2(bitmask)

    return [(bitmask & (1<<i)) != 0 for i in xrange(min_i, max_i)]


def bl2bm(booleans):
    '''
    convert a list of booleans to a bitmask
    '''
    return sum([(1<<i) for i, b in enumerate(booleans) if b])



def bl2i(booleans):
    '''
    convert a list of booleans to a list of indices
    '''
    return [i for i, b in enumerate(booleans) if b]


def i2bl(indices, length=None):
    '''
    convert a list of indices to a list of booleans
    '''
    min_i, max_i = min(indices), max(indices)
    ret = [i in indices for i in xrange(min_i, max_i+1)]

    while len(ret) < length:
        ret = [False,] + ret

    return ret

