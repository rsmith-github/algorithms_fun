import unittest


def isSubsequence(s, t):
    
    pass

class TestIsSubsequence(unittest.TestCase):
    
    
    def test_is_subsequence_1(self):
        
        self.assertEqual(isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(isSubsequence("ace", "abcde"), True)
        self.assertEqual(isSubsequence("axc", "ahbgdc"), False)
        

if __name__ == "__main__":
    unittest.main()