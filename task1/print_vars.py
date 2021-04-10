import sys


def print_vars():
    # get second frame from call stack
    frame = sys._getframe(1)
    # function that checks the type of a variable
    is_builtin_class_instance = lambda obj: obj.__class__.__module__ == "builtins"
    # loop over all frame variables
    for var, val in frame.f_locals.items():
        print(f"{var}: {is_builtin_class_instance(val)}")
