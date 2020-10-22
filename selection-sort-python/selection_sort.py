"""
Time complexity: 
    Worst case: [Big-O] O(n^2)
    Average case: [Big-theta] ⊝(n^2)
    Best case: [Big-Omega] Ω(n^2)

How it works:

- find the position of the minimum element;
- swap this element with the first one (because in the sorted array it should be the first);
- now regard the sub-array of length N-1, without the last value (which is already "in right place");
- find the position of maximum element in this sub-array (i.e. second to maximum in the whole array);
- swap it with the last element in the sub-array (i.e. with position N-2);
- now regard the sub-array of the length N-2 (without two last elements);
- algorithm ends when "sub-array" decreases to the length of 1.

About: 
    inefficient on large lists
    worse than insertion sort

Variants:
    Heapsort: 
        uses implicit heap data structure to speed up finding and removing the lowest datum, is faster with the same basic idea
    Bingo sort:
        items are ordered by repeatedly looking through the remaining items to find the greatest value and moving all items with that value to their final location.
"""
import argparse
import logging
from typing import Any, Iterable, TypeVar

logger = logging.getLogger(__name__)


def selection_sort_first_try(array: Iterable) -> Iterable:
    """Uses maximums, not minimums, also recursive, not the usual way it would be done"""
    if len(array) <= 1:
        return array
    max_index = array.index(max(array))
    array[-1], array[max_index] = array[max_index], array[-1]
    array[:-1] = selection_sort(array[:-1])
    return array


def selection_sort(array: Iterable) -> Iterable:
    """In place sorting algorithm that is simple but inefficient"""
    for i in range(len(array)):

        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
    return array


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sort elements using Selection Sort algorithm"
    )
    parser.add_argument('values', metavar='V', type=int,
                        nargs='+', help='values to sort')
    array = parser.parse_args().values
    length = len(array)
    sorted_array = selection_sort(array)
    print(
        f"out: {sorted_array};\narray_length: {length};"
    )
