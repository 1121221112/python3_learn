# *_*coding:utf-8 *_*


def same_obj_ref():
    a = [1, 2, 3]
    b = a
    a.append(4)
    print(b)
    print(id(b) == id(a))


class Gizmo:

    def __init__(self):
        print("Gizmo id : %d " % id(self))


def obj_id():
    x = Gizmo()
    print(dir(x))


def idef_equal():
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    # lewis 是 charles 的别名指向同一个对象
    lewis = charles
    print(lewis is charles)
    print(id(lewis), id(charles))
    lewis['balance'] = 950
    print(charles)

    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    # alex 是一个新的对象，但因为内部的__eq__方法导致 == 值判断 相等
    print(alex == charles)
    print(alex is not charles)
    '''
    == 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识
    在变量和单例值之间比较时，应该使用 is。目前，最常使用 is 检查变量绑定的值是不是 None。下面是推荐的写法：
        x is None
    is 运算符比 == 速度快，因为它不能重载，所以 Python 不用寻找并调用特殊方法，而是直接比较两个整数 ID。而 a == b 是语法糖，
    等同于 a.__eq__(b)。继承自 object 的 __eq__方法比较两个对象的 ID，结果与 is 一样。但是多数内置类型使用更有意义的方式覆盖了__eq__ 方法，
    会考虑对象属性的值。
    '''


def relative_immutability_tuples():
    """
    元组与多数 Python 集合（列表、字典、集，等等）一样，保存的是对象的引用。 1 如果引用的元素是可变的，即便元组本身不可变，元素依然可变。
    也就是说，元组的不可变性其实是指 tuple 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关
    """
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    print(t1 == t2)
    print(id(t1[-1]))
    t1[-1].append(99)
    print(t1)
    print(id(t1[-1]))
    print(t1 == t2)


if __name__ == '__main__':
    # same_obj_ref()
    # obj_id()
    # idef_equal()
    relative_immutability_tuples()
