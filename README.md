# bitmin
A Python module for bitmask handling/conversion

---

This module contains a set of converters for converting bitmasks (`bm`), indices(`i`), and boolean lists (`bl`) into eachother.

So instead of using the bitwise shift operator, `<<`, directly, like so

    for i in xrange(min_i, max_i)
        if (bitmask & (1<<i))]
            do_something_with(i)

one can do this

    for i in bm2i(bitmask)
        do_something_with(i)

The generated boolean lists can be used in conjunction with Numpy's [boolean array indexing](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#boolean-array-indexing).

---

Additionally, three "appliers" are available returning a list filtered according to the bitmask/indices/boolean list:

    apply_bm(49780, range(17)) == [2, 4, 5, 6, 9, 14, 15]

See the enclosed `example.py` for how to use the module.
