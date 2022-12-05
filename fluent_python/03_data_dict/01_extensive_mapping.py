# *_*coding:utf-8 *_*
import collections
import sys
import re

from types import MappingProxyType


def hashDemo():
    tt = (1, 2, (3, 4))
    print(hash(tt))
    # t1 = (1, 2, [3, 4])
    # print(hash(t1))
    t2 = (1, 2, frozenset([3, 4]))
    print(hash(t2))


DIAL_CODES = [(86, 'China'),
              (91, 'India'),
              (1, 'United States'),
              (62, 'Indonesia'),
              (55, 'Brazil'),
              (92, 'Pakistan'),
              (880, 'Bangladesh'),
              (234, 'Nigeria'),
              (7, 'Russia'),
              (81, 'Japan'), ]


def dictDemo():
    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code)
    code2 = {code: country.upper() for country, code in country_code.items() if code < 66}
    print(code2)


def dictKSetDefault():
    test_dict = {country: code for code, country in DIAL_CODES}
    print(test_dict)
    # 普通方法，判断建是否存在字典中，不存在新增，避免获取键直接错误
    # if "Beijing" not in test_dict.keys():
    #     test_dict["Beijing"] = 0
    # setdefault方法 默认设置为0
    test_dict.setdefault("Beijing", 0)
    print(test_dict)
    dd = collections.defaultdict(list)
    print(dd["AA"])


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


def missingDemo():
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d["2"])
    ct = collections.Counter("abracadabra")
    print(ct)
    ct.update("aaaaazzz")
    print(ct)
    print(ct.most_common(2))


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


def mappingProxyDemo():
    # immutable mapping
    d = {1: "A"}
    d_proxy = MappingProxyType(d)
    print(d_proxy)
    print(d_proxy[1])
    d[2] = "B"
    print(d_proxy)


if __name__ == '__main__':
    # hashDemo()
    # dictDemo()
    # dictKSetDefault()
    # missingDemo()
    mappingProxyDemo()
