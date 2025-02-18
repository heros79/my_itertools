from inspect import isfunction
from typing import Iterable, Generator


def accumulate(iterable: Iterable, fn=None) -> Generator:
    data = iter(iterable)
    if fn is None and not isfunction(fn):
        fn = lambda a, b: a + b
    f_sum = next(data)
    yield f_sum
    for i in data:
        f_sum = fn(f_sum, i)
        yield f_sum





