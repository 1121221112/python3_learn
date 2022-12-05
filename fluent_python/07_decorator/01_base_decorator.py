# *_*coding:utf-8 *_*

def deco(func):
    def inner():
        print("running inner()")
    # 注意返回为inner 对象不是 inner()
    return inner


@deco
def target():
    print("running target()")


if __name__ == '__main__':
    target()
    print(target)
