# *_*coding:utf-8 *_*

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def average_oo():
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager


def make_averager_demo():
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents)


def new_make_averager():
    count, total = 0, 0

    def averager(new_value):
        nonlocal count, total  # 借助nonlocal 变成自由变量，避免不可变类型，局部变量
        count += 1
        total += new_value
        return total / count

    return averager


def new_make_averager_demo():
    new_avg = new_make_averager()
    print(new_avg(10))
    print(new_avg(11))
    print(new_avg(12))
    print(new_avg.__code__.co_varnames)
    print(new_avg.__code__.co_freevars)
    print(new_avg.__closure__)
    print(new_avg.__closure__[0].cell_contents)


if __name__ == '__main__':
    # average_oo()
    # make_averager_demo()
    new_make_averager_demo()
