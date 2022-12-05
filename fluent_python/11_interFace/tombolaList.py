# *_*coding:utf-8 *_*


from random import randrange

from tombloa import Tombola


@Tombola.register
class TomblaList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    print(issubclass(TomblaList, Tombola))

    t = TomblaList(range(100))
    print(isinstance(t, Tombola))
