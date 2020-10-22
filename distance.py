from dataclasses import dataclass, field
from functools import update_wrapper, wraps
from time import perf_counter


class Monitor:
    """
        Timing the execution of a function
    """
    
    def __init__(self, function):
        self.time = perf_counter()
        update_wrapper(self, function)
        self.function = function

    def __call__(self, *args, **kwargs):
        value = self.function(*args, **kwargs)
        ended = perf_counter()
        self.time, self.function.time = (time := round(ended - self.time, 3)), time
        return value


def timer(func: object) -> object:
    """
        Timing the execution of a function
    """
    @wraps(func)
    def inner_time(*args, **kwargs):
        time_st = perf_counter()
        return_v = func(*args, **kwargs)
        time_ed = perf_counter()
        inner_time.time = time_ed - time_st
        return return_v
    return inner_time


@timer
@dataclass(order=True)  # By setting order to be true will allow me to perform comparison on the class object
class Distance:
    sort: int = field(init=False, repr=False)  # This will be the main data for the comparison which is generated automatically from post init
    x: int = field(default=0)
    y: int = field(default=0)

    def __post_init__(self):
        self.sort = self.x + self.y

    @timer
    def distance(self, other: object) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y)) ** 0.5

    def __sub__(self, other):
        return Distance((self.x - other.x), (self.y - other.y))


if __name__ == '__main__':
    d1 = Distance(8, 9)
    # print(d1.time)
    d2 = Distance(11, 3)
    d3 = Distance()
    print('d2 > d1', d2 > d1)
    print('d2 >= d1', d2 >= d1)
    print('d2 < d1', d2 < d1)
    print('d2 <= d1', d2 <= d1)
    print((d2 - d1))
    # print(isinstance(d2, Distance))
    print()
    print(d1.distance(d2))
