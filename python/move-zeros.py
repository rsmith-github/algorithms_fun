import unittest


def moveZeros(list):
    
    i = 0
    
    # move all non-zero elements to the start
    for j in range(len(list)):
        if list[j] != 0:
            list[i] = list[j]
            i += 1
    
    # set remaining elements to 0
    for j in range(i, len(list)):
        list[j] = 0
    

class TestMoveZeros(unittest.TestCase):
    
    def test_move_zeros(self):
        input = [0,1,0,3,12]
        moveZeros(input)
        self.assertEqual(input, [1,3,12,0,0])
        
    def test_move_zeros_1(self):
        input = [0,2,5,3,12]
        moveZeros(input)
        self.assertEqual(input, [2,5,3,12,0])

    def test_move_zeros_2(self):
        input = [0]
        moveZeros(input)
        self.assertEqual(input, [0])
        
    def test_move_zeros_3(self):
        input = [0,9]
        moveZeros(input)
        self.assertEqual(input, [9,0])
        

if __name__ == "__main__":
    unittest.main()