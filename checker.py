from dataclasses import dataclass, field
from itertools import zip_longest


def check(a, b):
	c = iter([(i - j) for i, j in zip(a, b)])
	return sum(c)
	

@dataclass
class Checker:
	c: tuple = field(repr=False, init=False, default=None)
	a: list
		
	def _test(self, other):
		def _innertest():
			se = iter([(i - j) for i, j in zip_longest(self.a, other.a, fillvalue=0)])
			ot = iter([(i - j) for i, j in zip_longest(other.a, self.a, fillvalue=0)])
			self.c = sum(se), sum(ot)
			return self.c

		if self.c is None:
			return _innertest()
		else:
			return self.c

	def __lt__(self, other):
		f, s = self._test(other)
		return f < s

	def __gt__(self, other):
		f, s = self._test(other)
		return f > s

	def __le__(self, other):
		f, s = self._test(other)
		return f <= s

	def __ge__(self, other):
		f, s = self._test(other)
		return f >= s


a = [12, 56, 71, 2]
b = [12, 32, 13, 8]
c = [242, 681, 12]
d = [2000, ]

x1 = Checker(a)
x2 = Checker(b)
x3 = Checker(c)
x4 = Checker(d)

y = check(a, b)

print( x2 > x1)

print(f'{x1}\n{x2}')
print(x2 < x3)

print(x2 > x1)
print(x2 < x4)
print(x4.c)
print(x2.c)
print(x2 > x1)

s = Checker([13, 12])
print(s < x2)