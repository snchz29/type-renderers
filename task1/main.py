import collections
import sys
import pandas

# Example
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


def print_vars():
    # get second frame from call stack
    frame = sys._getframe(1)
    # function that checks the type of a variable
    is_builtin_class_instance = lambda obj: obj.__class__.__module__ == "builtins"
    # loop over all frame variables
    for var, val in frame.f_locals.items():
        print(f"{var}: {is_builtin_class_instance(val)}")


if __name__ == '__main__':
    foo()
