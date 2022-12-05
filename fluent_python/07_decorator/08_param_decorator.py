# *_*coding:utf-8 *_*


registry = []


def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")


def main():
    print("running main()")
    print("registry ->", registry)
    f1()


new_registry = set()


def new_register(active=True):
    def decorate(func):
        print("running register(active=%s)->decorate(%s)" % (active, func))
        if active:
            new_registry.add(func)
        else:
            new_registry.discard(func)
        return func

    return decorate


@new_register(active=True)
def f2():
    print('running f2()')


@new_register(active=False)
def f3():
    print('running f3()')


def new_main():
    f2()
    f3()


if __name__ == '__main__':
    # main()
    new_main()