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
        self.assertEqual(can_place_flowers([0,0,0,0,0], 2), True)  # All empty, can place 2 flowers
        self.assertEqual(can_place_flowers([1,0,0,0,0,0,1], 2), True)  # Multiple empty slots at the end
        self.assertEqual(can_place_flowers([1,0,0,0,1,0,0], 1), True)  # Single place at the end
        self.assertEqual(can_place_flowers([0,0,0,0,1,0,0,0,0], 3), True)  # Can place 3 flowers in between
        self.assertEqual(can_place_flowers([1,0,0,0,0,1,0,0], 1), True)  # Place one in the middle
        self.assertEqual(can_place_flowers([1,0,0,0,0,1,0,0], 2), True)  # Can't place two in the middle
        self.assertEqual(can_place_flowers([1,0,0,0,0,1,0,0], 3), False)  # Can't place two in the middle
        self.assertEqual(can_place_flowers([0], 1), True)  # Single slot empty
        self.assertEqual(can_place_flowers([1], 1), False)  # Single slot occupied
        self.assertEqual(can_place_flowers([0,0,0], 2), True)  # Three slots, can place 2 flowers
        self.assertEqual(can_place_flowers([0,0,0], 1), True)  # Three slots, can place 1 flowers
        self.assertEqual(can_place_flowers([0,0,0], 3), False)  # Three slots, cannot place 3 flowers
        self.assertEqual(can_place_flowers([0,0,1,0,0,0], 2), True)  # Place two flowers in mixed slots
        self.assertEqual(can_place_flowers([0,0,0,0,0,0,0,0], 4), True)  # Place four flowers in long empty array
        self.assertEqual(can_place_flowers([1,0,0,0,0,0,0,0,1], 3), True)  # Long array with ends occupied
        


if __name__ == "__main__":
    unittest.main()