import unittest


def productExceptSelf(nums):
    
    # declare variables
    prefix = []
    suffix = []
    
    result = []
    
    # get prefix array
    left = 1
    for num in nums:
        left *= num
        prefix.append(left)
    
    # get suffix array
    right = 1
    for i in range(len(nums)-1, -1, -1):
        right *= nums[i]
        suffix.append(right)
    
    suffix.reverse()
    
    
    # multiply each position by previous index of the prefix array and next index of the suffix array
    for i in range(len(nums)):
        if i == 0:
            res_num = 1 * suffix[i+1]
        elif i == len(nums) - 1:
            res_num = 1 * prefix[i-1]
        else:
            res_num = suffix[i+1] * prefix[i-1]
            
        result.append(res_num)

    return result
    
    



class TestProductExceptSelf(unittest.TestCase):

    def test_product_except_self(self):
        self.assertEqual(productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])


if __name__ == "__main__":
    unittest.main()
