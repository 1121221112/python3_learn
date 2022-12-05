# *_*coding:utf-8 *_*
import unicodedata
from functools import reduce, partial
from operator import mul, itemgetter, attrgetter, methodcaller
from collections import namedtuple


def fact(n):
    # return reduce(lambda a, b: a*b, range(1, n+1))
    return reduce(mul, range(1, n + 1))


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def itemgetterDemo():
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)

    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))


def attrgettrDemo():
    LatLong = namedtuple("LatLong", "lat long")
    Metropolis = namedtuple("Metropolis", 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)
    name_lat = attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))


def methodcallerDemo():
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))
    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s))


def partialDemo():
    triple = partial(mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 10))))
    nfc = partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1, s2)
    print(s1 == s2)
    print(nfc(s1) == nfc(s2))


if __name__ == '__main__':
    # fact(1)
    # itemgetterDemo()
    # attrgettrDemo()
    # methodcallerDemo()
    partialDemo()
