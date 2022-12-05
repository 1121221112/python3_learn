# *_*coding:utf-8 *_*


def f(a, b):
    a += b
    return a


def fDemo():
    # 函数可能会修改接收到的任何可变对象
    x = 1
    y = 2
    print(f(x, y))  # 数字x没变
    print(x, y)

    a = [1, 2]
    b = [3, 4]
    print(f(a, b))  # 列表a变了
    print(a, b)

    t = (10, 20)
    u = (30, 40)
    print(f(t, u))  # 元组t未变
    print(t, u)


class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def HauntedBusDemo():
    bus1 = HauntedBus(['Alice', 'Bill'])
    print(bus1.passengers)
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(bus1.passengers)

    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print(bus2.passengers)

    bus3 = HauntedBus()
    print(bus3.passengers)

    bus3.pick('Dave')
    print(bus2.passengers)
    print(bus2.passengers is bus3.passengers)  # bus2 和 bus3 的乘客列表为同一列表

    print(bus1.passengers)

    '''
    默认值在定义函数时计算（通常在加载模块时），因此默认值变成了函数对象的属性。
    因此，如果默认值是可变对象，而且修改了它的值，那么后续的函数调用都会受到影响。
    '''


class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # self.passengers = passengers  # 非参数副本，导致可变参数外界丢参
            self.passengers = list(passengers)  # 避免影响传入参数

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def defense_variable_parameter():
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    bus.drop('Tina')
    bus.drop('Pat')
    print(bus.passengers)
    print(basketball_team)  # 非可变参数列表副本


if __name__ == '__main__':
    # fDemo()
    # HauntedBusDemo()
    defense_variable_parameter()
