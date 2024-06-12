import unittest


def isSubsequence(s, t):
    
    current_char = s[0]
    
    count = 0 
    
    for char in t:
        
        if current_char == char:
            
            if count == len(s) - 1:
                return True
            
            count += 1
            current_char = s[count]
    
    return count == len(s)
    
    

class TestIsSubsequence(unittest.TestCase):
    
    
    def test_is_subsequence_1(self):
        
        self.assertEqual(isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(isSubsequence("ace", "abcde"), True)
        self.assertEqual(isSubsequence("axc", "ahbgdc"), False)
        

if __name__ == "__main__":
    unittest.main()