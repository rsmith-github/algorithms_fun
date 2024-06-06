import unittest




def kids_with_candies(candies):
    
    return 0


class TestCandies(unittest.TestCase):
    
    def test_kids_with_candies(self):
        
        self.assertEqual(kids_with_candies([2,3,5,1,3]), 3)
        self.assertEqual(kids_with_candies([4,2,1,1,2]), 1)
        self.assertEqual(kids_with_candies([12,1,12]), 10)
        
if __name__ == "__main__":
    unittest.main()