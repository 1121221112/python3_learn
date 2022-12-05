# *_*coding:utf-8 *_*
import array
import struct


def codeEncodeDemo():
    s = 'café'
    print(len(s))
    b = s.encode('utf8')
    print(b)
    print(len(b))
    print(b.decode('utf8'))


def bytesDemo():
    cafe = bytes('café', encoding='utf_8')
    print(cafe)
    print(cafe[0])
    print(cafe[:1])
    cafe_arr = bytearray(cafe)
    print(cafe)
    print(cafe[-1:])


def arrayByteDemo():
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    octets = bytes(numbers)
    print(octets)


def memoryStruct():
    fmt = '<3s3sHH'
    with open('filter.gif', 'rb') as fp:
        img = memoryview(fp.read())
    header = img[:10]
    print(bytes(header))
    print(struct.unpack(fmt, header))
    del header
    del img


def bomDemo():
    u16 = 'El Niño'.encode('utf_16')
    print(u16)
    print(list(u16))


if __name__ == '__main__':
    # codeEncodeDemo()
    # bytesDemo()
    # arrayByteDemo()
    # memoryStruct()
    bomDemo()
