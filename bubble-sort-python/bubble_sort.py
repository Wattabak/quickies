"""
Time complexity
    Worst case: [Big-O] O(n^2)
    Average case: [Big-theta] ⊝(n^2)
    Best case: [Big-Omega] Ω(n)

Big help: 
    https://stackoverflow.com/questions/21272497/is-this-most-efficient-to-bubble-sort-a-list-in-python
    https://en.wikipedia.org/wiki/Bubble_sort

Further optimizations with the same idea: 
    Cocktail shaker sort, https://en.wikipedia.org/wiki/Cocktail_shaker_sort
"""
import argparse
import logging
from typing import Any, Iterable, TypeVar

logger = logging.getLogger(__name__)


def bubble_sort(array: Iterable) -> Iterable:
    """The simplest sorting algorithm

    Repeatedly swap the adjacent elements if they are in wrong order.

    Mathematically speaking, for any indexes i and j if i < j then a[i] <= a[j].

    n-th pass finds the n-th largest element and puts it into its final place

    also elements after the last swap on every pass will be sorted, because there were no swaps after it, so we can omit checking these
    """

    n = len(array)
    while n >= 1:
        newn = 0
        for i in range(1, n):

            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                newn = i

        n = newn
    return array


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sort elements using Bubble Sort algorithm"
    )
    parser.add_argument('values', metavar='V', type=int,
                        nargs='+', help='values to sort')
    array = parser.parse_args().values
    length = len(array)
    sorted_array = bubble_sort(array)
    print(
        f"out: {sorted_array}; array_length: {length};"
    )
