import collections

import pandas

from print_vars import print_vars


class MyClass:
    pass


def foo():
    a = 1
    b = MyClass()
    c = [1, 2, 3]
    d = pandas.DataFrame()
    e = {"a": pandas.Series(dtype="float64")}
    f = collections.Counter()
    g = False
    print_vars()


if __name__ == '__main__':
    foo()
