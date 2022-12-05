# *_*coding:utf-8 *_*

import weakref


def bye():
    print('Gone with the wind...')


def collectionDemo():
    s1 = {1, 2, 3}
    s2 = s1
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)


def weakReference():
    a_set = {0, 1}
    wref = weakref.ref(a_set)
    print(wref)
    print(wref())
    a_set = {2, 3, 4}
    print(wref())


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


def WeakValueDictionaryDemo():
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
               Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese

    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))


if __name__ == '__main__':
    # collectionDemo()
    # weakReference()
    WeakValueDictionaryDemo()
