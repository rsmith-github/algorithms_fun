import unittest


def can_place_flowers(flowerbed, n):
    
    
    for i in range(len(flowerbed)):
        # last element
        if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            n -= 1
        elif ( i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 ) or ( flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 ): # first element or in between
            n -= 1
            flowerbed[i] = 1 

    return n <= 0

    




class TestCanPlaceFlowers(unittest.TestCase):
    
    def test_can_place_flowers(self):
        
        self.assertEqual(can_place_flowers([1,0,0,0,1], 1), True)
        self.assertEqual(can_place_flowers([1,0,0,0,1], 2), False)
        self.assertEqual(can_place_flowers([0,0,1,0,1], 1), True)
        self.assertEqual(can_place_flowers([0,0,1,0,1,0,0,1,0,1], 1), True)
        self.assertEqual(can_place_flowers([0,0,1,0,1,0,0,1,0,1], 2), False)
        self.assertEqual(can_place_flowers([0,0,1,0,1,0,0,1,0,1], 3), False)
        
        


if __name__ == "__main__":
    unittest.main()