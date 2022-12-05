# *_*coding:utf-8 *_*

from array import array
from random import random


def memView():
    numbers = array("h", [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])

    memv_oct = memv.cast("B")
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)


if __name__ == '__main__':
    memView()
