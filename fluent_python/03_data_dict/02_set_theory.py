# *_*coding:utf-8 *_*

def setDemo():
    l = ["spam", "spam", "eggs", "spam"]
    print(set(l))
    print(list(set(l)))


def needlesNumInHaystack():
    needles = {"s", "b"}
    haystack = {"i", "s", "y"}
    found = 0
    for n in needles:
        if n in haystack:
            found += 1
    print(found)
    print(len(needles & haystack))
    print(len(set(needles).intersection(haystack)))


def buildSetDemo():
    from dis import dis
    print(dis('{1}'))
    print(dis('set([1])'))
    print(frozenset(range(10)))


def setcompsDemo():
    from unicodedata import name
    print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})


# 世界人口数量前10位国家的电话区号
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]


def dialCodesDemo():
    d1 = dict(DIAL_CODES)
    print('d1:', d1.keys())
    d2 = dict(sorted(DIAL_CODES))
    print('d2:', d2.keys())
    d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
    print('d3:', d3.keys())


if __name__ == '__main__':
    # setDemo()
    # needlesNumInHaystack()
    # buildSetDemo()
    # setcompsDemo()
    dialCodesDemo()
