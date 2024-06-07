import unittest


def productExceptSelf(nums):
    
    # declare variables
    
    # get prefix array
    
    
    # get suffix array
    
    
    # multiply each position by previous index of the prefix array and next index of the suffix array
    
    pass
    
    



class TestProductExceptSelf(unittest.TestCase):

    def test_product_except_self(self):
        self.assertEqual(productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])
        # self.assertEqual(mergeAlternately('ab', 'pqrs'), 'apbqrs')


if __name__ == "__main__":
    unittest.main()
