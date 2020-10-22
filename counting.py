#!/bin/env python
from time import perf_counter
from functools import wraps


def timer(_func=None, *, approx=None):
	def inner_timer(func: object) -> object:
		@wraps(func)  # Protecting the behaviour of the wrapped function
		def wrapper_timer(*args, **kwargs):
			time_started = perf_counter()
			value = func(*args, *kwargs)
			duration = perf_counter() - time_started
			print(f"{func.__name__}'s duration: {round(duration, approx)} sec")
			return value
		return wrapper_timer

	if _func is None:
		return inner_timer  # If approx argument is not use
	return inner_timer(_func)  # The arguement is  use


@timer(approx=10)
def count(start, end, /, *, step=1):
	while start <= end:
		yield start
		start += step


if __name__ == '__main__':
	c = count(1, 9)
	range = timer(range, approx=20)  # Modifying the behaviour of the in-built range method
	# Approximating the return value to be in 20dp.
	r = range(1, 9)
	for i in c:
		print('c:', i)
	for j in r:
		print('r', j)
	print(type(c))
	print(type(r))
