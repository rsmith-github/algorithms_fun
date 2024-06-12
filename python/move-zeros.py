import unittest


def moveZeros(list):
    pass

class TestMoveZeros(unittest.TestCase):
    
    def test_move_zeros(self):
    
        input = [0,1,0,3,12]
        moveZeros(input)
        self.assertEqual(input, [1,3,12,0,0])
        

if __name__ == "__main__":
    unittest.main()