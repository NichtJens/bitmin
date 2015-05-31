#!/usr/bin/env python


from bitmin import *


inp = [2, 4, 5, 6, 9, 14, 15]
print inp

bm = i2bm(inp)
print bm, bin(bm)



max_i = next_heigher_power_of_2(bm)
for i in xrange(max_i):
    print i, "y" if (bm & (1<<i)) else "n"






assert bm2i(bm) == inp

bl = bm2bl(bm)
print bl

assert bl2bm(bl) == bm


assert bl2i(bl) == inp
print i2bl(inp)
print i2bl(inp, 16)
assert i2bl(inp, 16) == bl





#print apply_bm(b, xrange(17))
#print apply_i(out, xrange(17))
#print apply_bl(out, xrange(17))




