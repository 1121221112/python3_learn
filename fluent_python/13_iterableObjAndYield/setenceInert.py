# *_*coding:utf-8 *_*
import os
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        """
        for match in RE_WORD.finditer(self.text):
            yield match.group()
            可简化生成器表达式如下
        """
        return (match.group() for match in RE_WORD.finditer(self.text))



