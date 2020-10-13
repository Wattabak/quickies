"""

Not very optimized currently

Big help: 
    https://stackoverflow.com/questions/21272497/is-this-most-efficient-to-bubble-sort-a-list-in-python
    https://en.wikipedia.org/wiki/Bubble_sort
"""
import argparse
import logging
from itertools import tee
from typing import Any, Iterable, TypeVar

logger = logging.getLogger(__name__)


Swaps = TypeVar(int)
Compares = TypeVar(int)


def bubble_sort(array: Iterable) -> tuple[Iterable, Swaps, Compares]:
    """The simplest sorting algorithm

    Repeatedly swap the adjacent elements if they are in wrong order.

    Mathematically speaking, for any indexes i and j if i < j then a[i] <= a[j].
    """

    swaps, compares = 0, 0
    while True:
        swapped = False
        for i in range(1, len(array)):

            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                swaps += 1
                swapped = True

            compares += 1

        if not swapped:
            break
    return array, swaps, compares


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sort elements using Bubble Sort algorithm"
    )
    parser.add_argument('values', metavar='V', type=int,
                        nargs='+', help='values to sort')
    array = parser.parse_args().values
    length = len(array)
    sorted_array, swpcount, cmpcount = bubble_sort(array)
    print(
        f"out: {sorted_array};\ncompares: {cmpcount};"
        f"\nswpcount: {swpcount};\narray_length: {length}"
    )
