# *_*coding:utf-8 *_*
import functools

from clock_decorator_05 import new_clock


@functools.lru_cache(maxsize=128, typed=False)
@new_clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(30))