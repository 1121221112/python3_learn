# *_*coding:utf-8 *_*


def simple_coroutine():
    print('-> croutine started')
    x = yield
    print('-> coroutine eceived:', x)


def demo1():
    my_coro = simple_coroutine()
    print(my_coro)
    # next(my_coro)
    my_coro.send(None)
    my_coro.send(42)


def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


def demo2():
    my_coro2 = simple_coro2(14)
    from inspect import getgeneratorstate
    print(getgeneratorstate(my_coro2))
    next(my_coro2)
    print(getgeneratorstate(my_coro2))
    my_coro2.send(28)
    my_coro2.send(99)
    print(getgeneratorstate(my_coro2))


if __name__ == '__main__':
    # demo1()
    demo2()
