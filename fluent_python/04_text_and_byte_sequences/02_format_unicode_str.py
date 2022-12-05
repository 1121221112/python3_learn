# *_*coding:utf-8 *_*
import re
import unicodedata
from unicodedata import normalize, name, combining


def unicodeDemo():
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(len(s1), len(s2))
    print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
    print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))

    ohm = '\u2126'
    print(name(ohm))
    ohm_c = normalize('NFC', ohm)
    print(name(ohm_c))
    print(ohm_c == ohm)
    print(normalize('NFC', ohm_c) == normalize('NFC', ohm))


def caseFoldDemo():
    micro = 'µ'
    print(name(micro))
    micro_cf = micro.casefold()
    print(name(micro_cf))
    print(micro, micro_cf)
    eszett = 'ß'
    print(name(eszett))
    eszett_cf = eszett.casefold()
    print(eszett, eszett_cf)


def nfc_equal(s1, s2):
    return normalize('NFC', s1) == normalize('NFC', s2)


def fold_equal(s1, s2):
    return normalize('NFC', s1).casefold() == normalize('NFC', s2).casefold()


def normeqDemo():
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1 == s2)
    print(nfc_equal(s1, s2))
    print(nfc_equal('A', 'a'))

    s3 = 'Straße'
    s4 = 'strasse'
    print(s3 == s4)
    print(nfc_equal(s3, s4))
    print(fold_equal(s3, s4))
    print(fold_equal(s1, s2))
    print(fold_equal('A', 'a'))


def shave_marks(txt):
    """去掉全部变音符号"""
    norm_txt = normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not combining(c))
    return normalize('NFC', shaved)


def sahveMarksDemo():
    order = '“ Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
    print(shave_marks(order))

    Greek = 'Zέφupoς, Zéfiro'
    print(shave_marks(Greek))


def unicodeDataDBDemo():
    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    for char in sample:
        print('U+%04x' % ord(char),
              char.center(6),
              re_digit if re_digit.match(char) else '-',
              'isdig' if char.isdigit() else '-',
              'isnum' if char.isnumeric() else '-',
              format(unicodedata.numeric(char), '5.2f'),
              unicodedata.name(char),
              sep='\t')


if __name__ == '__main__':
    # unicodeDemo()
    # caseFoldDemo()
    # normeqDemo()
    # sahveMarksDemo()
    unicodeDataDBDemo()
