import unittest


def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    big = max(candies)

    return [i + extraCandies >= big for i in candies]


class TestKidsWithCandies(unittest.TestCase):

    def test_kids_with_candies(self):
        self.assertEqual(kidsWithCandies([2, 3, 5, 1, 3], 3), [
                         True, True, True, False, True])
        self.assertEqual(kidsWithCandies([4, 2, 1, 1, 2], 1), [
                         True, False, False, False, False])


if __name__ == "__main__":
    unittest.main()
