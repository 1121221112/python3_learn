# *_*coding:utf-8 *_*

from collections import namedtuple

Result = namedtuple('Result', 'count average')


def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def demoFirst():
    coro_avg = average()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    # coro_avg.send(None)


def catchStopVal():
    coro_avg = average()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value
    print(result)


if __name__ == '__main__':
    # demoFirst()
    catchStopVal()

