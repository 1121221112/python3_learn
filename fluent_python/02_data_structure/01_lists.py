# *_*coding:utf-8 *_*
import array


def list_prod(ascis=""):
    # 列表推导和生成器表达式
    # 写法1
    # codes = []
    # for s in ascis:
    #     codes.append(ord(s))
    # 写法2
    codes = [ord(s) for s in ascis]
    print(codes)


def list_map(ascis=""):
    # 列表推导和map/filter组合
    # 写法1
    # beyond_assci = [ord(s) for s in ascis if ord(s) > 127]
    # 写法2
    beyond_assci = list(filter(lambda x: x > 127, map(ord, ascis)))
    print(beyond_assci)


def list_tulpe_prod(ascis=""):
    # 用生成器表达式 初始化元组和数组
    print(tuple(ord(s) for s in ascis))
    print(array.array("I", (ord(s) for s in ascis)))


if __name__ == '__main__':
    symbols = "$¢£¥€¤"
    # list_prod(symbols)
    # list_map(symbols)
    list_tulpe_prod(symbols)
