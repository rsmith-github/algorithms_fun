import unittest


def container_with_most_water(list):
    
    
    # keep track of current max area
    
    
    # two pointer while loop
    
        # if left bar is lower or equal to right bar, calculate area and move left pointer
        
        
        # if right bar is lower or equal to left bar, calculate area and move right pointer
        
    
    # return max area
    pass


class TestCointainerWithMostWater(unittest.TestCase):
    
    def test_container_with_most_water(self):
        
        self.assertEqual(container_with_most_water[[1,8,6,2,5,4,8,3,7]], 49)
        self.assertEqual(container_with_most_water[[1]], 1)
        self.assertEqual(container_with_most_water[[6,7,1,2,3,6]], 30)
        
        
if __name__ == "__main__":
    unittest.main()