import unittest


def container_with_most_water(heights):
    
    l = 0
    r = len(heights) - 1
    # keep track of current max area
    c_max = 0

    # two pointer while loop
    while l < r:
        # if left bar is lower or equal to right bar, calculate area and move left pointer
        if heights[l] <= heights[r]:
            area = heights[l] * (r - l)
            l += 1
        # if right bar is lower or equal to left bar, calculate area and move right pointer
        elif heights[r] <= heights[l]:
            area = heights[r] * (r - l)
            r -= 1
        # update max area
        if c_max < area: c_max = area
    
    # return max area
    return c_max
    

class TestCointainerWithMostWater(unittest.TestCase):
    
    def test_container_with_most_water(self):
        
        self.assertEqual(container_with_most_water([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(container_with_most_water([1,1]), 1)
        self.assertEqual(container_with_most_water([6,7,1,2,3,6]), 30)
        
        
if __name__ == "__main__":
    unittest.main()