
#import itertools


def apply_bm(bitmask, d):
    '''
    apply a bitmask to an iterable d
    '''
    return [item for i, item in enumerate(d) if (bitmask & (1<<i))]


def apply_i(indices, d):
    '''
    apply a list of indices to an iterable d
    '''
    return [item for i, item in enumerate(d) if i in indices]


def apply_bl(booleans, d):
    '''
    apply a list of booleans to an iterable
    '''
    return [item for flag, item in zip(booleans, d) if flag]
#    return list(itertools.compress(d, booleans))

