# Type Renreders

## Task 1

The task1 branch implements the `print_vars()` function in Python, which parses local variables in the scope from which it was called. For each variable, its name and the result of checking whether it is a built-in type or not are displayed.

### Example:
```python
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
```

```
a: True
b: False
c: True
d: False
e: True
f: False
g: True
```

## Task 2

The task2 branch contains a Java console application. It takes the path to the Python interpreter and executes the following command `<python-path> m timeit -r 10`, where \<python-path\> -- the string that the user entered. While waiting, the number of seconds from the start is displayed. At the end of the process, its result is also displayed.

### Example

```
Python interpreter path: /usr/bin/python3
Time elapsed: 1s
Time elapsed: 2s
Time elapsed: 3s
Time elapsed: 4s
Time elapsed: 5s
50000000 loops, best of 10: 8.45 nsec per loop
```