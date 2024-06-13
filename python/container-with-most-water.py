import unittest


def container_with_most_water(list):
    
    pass


class TestCointainerWithMostWater(unittest.TestCase):
    
    def test_container_with_most_water(self):
        
        self.assertEqual(container_with_most_water[[1,8,6,2,5,4,8,3,7]], 49)
        self.assertEqual(container_with_most_water[[1]], 1)
        self.assertEqual(container_with_most_water[[6,7,1,2,3,6]], 30)
        
        
if __name__ == "__main__":
    unittest.main()