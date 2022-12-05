# *_*coding:utf-8 *_*
import copy


def shallow_copy():
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)  # l2 是 l1的浅复制副本
    l1.append(100)  # 将100 追加到l1中，对l2没有影响
    l1[1].remove(55)  # 把l1[1] 中的55 删除。对l2有影响，因为l2[1]和l1[1]绑定的是同一个列表
    print('l1: ', l1)
    print('l2: ', l2)
    l2[1] += [33, 22]  # 对可变的对象来说，如 l2[1] 引用的列表， += 运算符就地修改列表。
    l2[2] += (10, 11)  # 对元组来说， += 运算符创建一个新元组，然后重新绑定给变量 l2[2]。
    print('l1: ', l1)
    print('l2: ', l2)


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def copy_deepcopy_demo():
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))  # 使用copy和deepcopy 创建3个不同实例
    bus1.drop('Bill')
    print(bus2.passengers)
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))  # bus1和bus2共享同一个列表对象
    print(bus3.passengers)


def deepcopyCycle():
    """
    注意，一般来说，深复制不是件简单的事。如果对象有循环引用，那么这个朴素的算法会进入无限循环。
    """

    a = [10, 20]
    b = [a, 30]
    a.append(b)
    print(a)
    from copy import deepcopy
    c = deepcopy(a)
    print(c)
    '''
    此外，深复制有时可能太深了。例如，对象可能会引用不该复制的外部资源或单例值。我们可以实现特殊方法 __copy__() 和 __deepcopy__()，控制 copy 和 deepcopy 的行为，详情参见 copy 模块的文档（ http://docs.python.org/3/library/copy.html）。
    '''


if __name__ == '__main__':
    # shallow_copy()
    # copy_deepcopy_demo()
    deepcopyCycle()
