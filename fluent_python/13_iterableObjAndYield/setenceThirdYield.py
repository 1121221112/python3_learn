# *_*coding:utf-8 *_*
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


def yieldDemo():
    yield 1
    yield 2
    yield 3


def yieldMsg():
    print('Start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


if __name__ == '__main__':
    yieldDemo()
    for i in yieldDemo():
        print(i)

    for c in yieldMsg():
        print('-->', c)