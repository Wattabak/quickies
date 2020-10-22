import random
import unittest

from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_almost_sorted(self) -> None:
        """80-90% sorted"""
        args = [1, 2, 4, 9, 5, 6, 50, 100]
        sorted_vals = insertion_sort(args)
        must_return = [1, 2, 4, 5, 6, 9, 50, 100]
        self.assertEqual(sorted_vals, must_return)

    def test_already_sorted(self) -> None:
        """Best case"""
        args = [0, 5, 10, 20, 21, 22, 22, 23, 40]
        sorted_vals = insertion_sort(args)
        must_return = [0, 5, 10, 20, 21, 22, 22, 23, 40]
        self.assertEqual(sorted_vals, must_return)

    def test_not_sorted(self) -> None:
        """Average case"""
        args = [20, 1, 35, 90, 3, 5, 2, 40, 1]
        sorted_vals = insertion_sort(args)
        must_return = [1, 1, 2, 3, 5, 20, 35, 40, 90]
        self.assertEqual(sorted_vals, must_return)

    def test_worst_case(self) -> None:
        args = [90, 40, 35, 20, 5, 3, 2, 1, 1]
        sorted_vals = insertion_sort(args)
        must_return = [1, 1, 2, 3, 5, 20, 35, 40, 90]
        self.assertEqual(sorted_vals, must_return)


if __name__ == "__main__":
    unittest.main()
