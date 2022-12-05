# *_*coding:utf-8 *_*


class DemoException(Exception):
    """演示异常类型"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received : {!r}'.format(x))
    raise RuntimeError('This line should never run.')


def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received : {!r}'.format(x))
    finally:
        print('-> coroutine ending')


def demo1():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    exc_coro.close()
    from inspect import getgeneratorstate
    print(getgeneratorstate(exc_coro))


def demo2():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(DemoException)
    from inspect import getgeneratorstate
    print(getgeneratorstate(exc_coro))


def demo3():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(ZeroDivisionError)
    from inspect import getgeneratorstate
    print(getgeneratorstate(exc_coro))


if __name__ == '__main__':
    # demo1()
    # demo2()
    demo3()
