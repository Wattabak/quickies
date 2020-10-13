import random
import unittest

from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_almost_sorted(self) -> None:
        args = [1, 2, 4, 9, 5, 6, 50, 100]
        sorted_vals, swpc, cmpc = bubble_sort(args)
        must_return = [1, 2, 4, 5, 6, 9, 50, 100]
        self.assertEqual(sorted_vals, must_return)

    def test_already_sorted(self) -> None:
        args = [0, 5, 10, 20, 21, 22, 22, 23, 40]
        sorted_vals, swpc, cmpc = bubble_sort(args)
        must_return = [0, 5, 10, 20, 21, 22, 22, 23, 40]
        self.assertEqual(sorted_vals, must_return)

    def test_not_sorted(self) -> None:
        args = [20, 1, 35, 90, 3, 5, 2, 40, 1]
        sorted_vals, swpc, cmpc = bubble_sort(args)
        must_return = [1, 1, 2, 3, 5, 20, 35, 40, 90]
        self.assertEqual(sorted_vals, must_return)


if __name__ == "__main__":
    unittest.main()
