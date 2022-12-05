# *_*coding:utf-8 *_*


def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def funcName():
    fact = factorial
    print(fact)
    print(fact(5))
    print(map(factorial, range(11)))
    print(list(map(fact, range(11))))


def higherOrderFunctions():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=reverse))


def reverse(word):
    return word[::-1]


if __name__ == '__main__':
    # print(factorial(42))
    # print(factorial.__doc__)
    # print(type(factorial))
    # funcName()
    higherOrderFunctions()
