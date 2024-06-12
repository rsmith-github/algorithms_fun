from ipaddress import ip_address
import unittest


def increasingTriplet(nums):
    pass

class TestIncreasingTriplets(unittest.TestCase):

    def test_increasingTriplet(self):
        self.assertEqual(increasingTriplet([1,2,3,4,5]), True)
        self.assertEqual(increasingTriplet([5,4,3,2,1]), False)
        self.assertEqual(increasingTriplet([2,1,5,0,4,6]), True)

if __name__ == "__main__":
    unittest.main()