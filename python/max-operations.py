import unittest

def max_operations(list, k):
    
    pass

class TestMaxOperations(unittest.TestCase):
    
    def test_max_operations(self):
        
        self.assertEqual(max_operations([1,8,6,2,5,4,8,3,7], 8), 3)
        self.assertEqual(max_operations([6,7,1,2,3,6], 8), 2)
        self.assertEqual(max_operations([1,2,3,4], 5), 2)
        
        
if __name__ == "__main__":
    unittest.main()