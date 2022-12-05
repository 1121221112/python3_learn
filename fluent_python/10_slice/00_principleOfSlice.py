# *_*coding:utf-8 *_*


class MySeq:
    def __getitem__(self, item):
        return item


if __name__ == '__main__':
    s = MySeq()
    print(s[1])
    print(dir(slice))
    print(help(slice.indices))
