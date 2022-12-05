# *_*coding:utf-8 *_*
import collections
from collections import namedtuple


def tulpeRecord():
    city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
    print(city, year, pop, chg, area)
    a, b, *reset = range(5)
    print(a, b, reset)


def namedTulpe():
    City = collections.namedtuple("CIty", "name country population coordinates")
    tokyo = City("Tokyo", "Jp", 36.933, (35.689, 139.691))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo.coordinates[1])
    print(City._fields)

    LatLong = namedtuple("LatLong", "lat long")
    delhi_data = ("Delhi NCR", "IN", "21.22", LatLong(11.21334, 77.043))
    delhi = City._make(delhi_data)
    print(delhi._asdict())
    for k, v in delhi._asdict().items():
        print(k + ": ", v)


if __name__ == '__main__':
    # tulpeRecord()
    namedTulpe()
