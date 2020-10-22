"""
Time complexity
    Worst case: [Big-O] O(n^2)
    Average case: [Big-theta] ⊝(n^2)
    Best case: [Big-Omega] Ω(n)

Space complexity: O(1)

Big help:
    https://www.programiz.com/dsa/insertion-sort
"""
import argparse
import logging
from typing import Any, Iterable

logger = logging.getLogger(__name__)


def insertion_sort(array: Iterable) -> Iterable:
    """
    For every iteration compare current element to every previous element,
         and change places with previous elements until the previous element is smaller
    """

    for i in range(1, len(array)):

        key = array[i]  # current element

        j = i-1  # previous element
        while j >= 0 and key < array[j]:
            # move the previous element to the current position
            array[j + 1] = array[j]
            j -= 1  # check previous pair
        array[j + 1] = key
    return array


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sort elements using Insertion Sort algorithm"
    )
    parser.add_argument('values', metavar='V', type=int,
                        nargs='+', help='values to sort')
    array = parser.parse_args().values
    length = len(array)
    sorted_array = insertion_sort(array)
    print(
        f"out: {sorted_array}; array_length: {length};"
    )
