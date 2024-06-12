import unittest


def increasingTriplet(nums):
    n1 = float('inf')
    n2 = float('inf')
    
    for n in nums:
        if n <= n1:
            n1 = n
        elif n <= n2:
            n2 = n
        else:
            return True
    
    return False


class TestIncreasingTriplets(unittest.TestCase):

    def test_increasingTriplet(self):
        self.assertEqual(increasingTriplet([1,2,3,4,5]), True)
        self.assertEqual(increasingTriplet([5,4,3,2,1]), False)
        self.assertEqual(increasingTriplet([2,1,5,0,4,6]), True)

if __name__ == "__main__":
    unittest.main()