# *_*coding:utf-8 *_*

class LookingClass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Pleasse DO NOT divide by zero!')
            return True


def LookDemo():
    with LookingClass() as what:
        print('Alice, kitty and Snowdrop')
        print(what)


if __name__ == '__main__':
    LookDemo()
