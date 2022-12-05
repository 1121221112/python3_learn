# *_*coding:utf-8 *_*

import numpy
from collections import deque


def numpyDemo():
    a = numpy.arange(12)
    print(a)
    print(type(a))
    print(a.shape)
    a.shape = 3, 4
    print(a)
    print(a[2])
    print(a[2, 1])
    print(a[:, 1])
    print(a.transpose())


def dequeDemo():
    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11, 22, 33])
    print(dq)
    dq.extendleft([10, 20, 30, 40])
    print(dq)


if __name__ == '__main__':
    # numpyDemo()
    dequeDemo()
