# *_*coding:utf-8 *_*
import bisect
import random
import sys
from array import array

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'
SIZE = 7


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


def insortDemo():
    random.seed(1729)
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print("%2d ->" % new_item, my_list)


def float_array():
    floats = array("d", (random() for i in range(10 ** 7)))
    print(floats[-1])
    fp = open("float.bin", "wb")
    floats.tofile(fp)
    fp.close()
    floats2 = array("d")
    fp = open("float.bin", "rb")
    floats2.fromfile(fp, 10 ** 7)
    fp.close()
    print(floats2[-1])
    print(floats2 == floats)


if __name__ == '__main__':
    if sys.argv[-1] is None:
        bisect_fn = bisect.bisect
    else:
        bisect_fn = bisect.bisect_left
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    insortDemo()
    float_array()
