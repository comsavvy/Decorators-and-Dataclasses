#!/bin/env python
from datetime import datetime as dt
import functools

__all__ = [
	'timer', 'total'
]


def timer(func):
	"""
	This will print the return value of the function and also the time it takes to execute.

	"""
	@functools.wraps(func)  # Wrapping the function to protect it behaviour
	def wrap_timer(*args, **kwargs):
		first = dt.now().microsecond
		value = func(*args, **kwargs)
		print('Result:', value)
		print(f"Execution time: {dt.now().microsecond - first}")
	return wrap_timer


@timer
def total(args):
	add = 0
	for i in args:
		add += i
	return add


if __name__ == '__main__':
	total([2, 3, 4, 6, 4])
	sum = timer(sum)
	sum([2, 3, 4, 6, 4])
