import unittest


def find_even_index(arr):

    return -1


class TestFindEvenIndex(unittest.TestCase):

    def test_basic_tests(self):
        self.assertEqual(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
        self.assertEqual(find_even_index([1, 100, 50, -51, 1, 1]), 1,)
        self.assertEqual(find_even_index([1, 2, 3, 4, 5, 6]), -1)
        self.assertEqual(find_even_index([20, 10, 30, 10, 10, 15, 35]), 3)
        self.assertEqual(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)
        self.assertEqual(find_even_index([10, -80, 10, 10, 15, 35, 20]), 6)
        self.assertEqual(find_even_index(list(range(1, 100))), -1)
        self.assertEqual(find_even_index(
            [0, 0, 0, 0, 0]), 0, "Should pick the first index if more cases are valid")
        self.assertEqual(find_even_index([-1, -2, -3, -4, -3, -2, -1]), 3)
        self.assertEqual(find_even_index(list(range(-100, -1))), -1)
        self.assertEqual(find_even_index([8, 8]), -1)
        self.assertEqual(find_even_index([8, 0]), 0)
        self.assertEqual(find_even_index([0, 8]), 1)
        self.assertEqual(find_even_index([7, 3, -3]), 0)
        self.assertEqual(find_even_index([8]), 0)
        self.assertEqual(find_even_index([10, -10]), -1)
        self.assertEqual(find_even_index([-3, 2, 1, 0]), 3)
        self.assertEqual(find_even_index(
            [-15, 5, 11, 17, 19, -17, 20, -6, 17, -17, 19, 16, -15, -6, 20, 17]), 8)


if __name__ == "__main__":
    unittest.main()
