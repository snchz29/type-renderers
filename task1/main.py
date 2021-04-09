import collections
import sys

import pandas


class MyClass:
    pass


def foo():
    a = 1
    b = MyClass()
    c = [1, 2, 3]
    d = pandas.DataFrame()
    e = {"a": pandas.Series()}
    f = collections.Counter()
    g = True
    print_vars()


def is_builtin_class_instance(obj):
    return obj.__class__.__module__ == "builtins"


def print_vars():
    frame = sys._getframe(1)
    for var, val in frame.f_locals.items():
        print(var, is_builtin_class_instance(val))


if __name__ == '__main__':
    foo()
