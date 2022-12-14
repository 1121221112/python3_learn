# *_*coding:utf-8 *_*
from functools import wraps


def cortine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@cortine
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


def demoAverage():
    coro_avg = average()
    next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))


def averUtilDemo():
    coro_avg = average()
    from inspect import getgeneratorstate
    print(getgeneratorstate(coro_avg))
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))


if __name__ == '__main__':
    # demoAverage()
    averUtilDemo()
