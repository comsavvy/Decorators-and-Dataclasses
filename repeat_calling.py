#!/bin/env python
import functools as ft


def repeat(_func=None, *, times_no=2):
    """
                Code for repeating function calls
        The function will be call 2 times by default,
        if the 'times_no' is specified the function will be call till the times_no is exhausted
    """
    
    def taken_func(func):
        @ft.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times_no):
                value = func(*args, **kwargs)
                print(value)
            return value
        return wrapper
    if _func is None:
        return taken_func
    else:
        return taken_func(_func)


@repeat
def add(*args):
    return sum(args)


if __name__ == '__main__':
    add(9, 2, 12, 82, 2, 1)
