# *_*coding:utf-8 *_*


b = 9


def f1(a):
    global b  # 不添加错误； b为局部变量
    print(a)
    print(b)
    b = 9


if __name__ == '__main__':
    f1(2)
