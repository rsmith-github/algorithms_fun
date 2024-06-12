import unittest


def isSubsequence(s, t):
    
    if s == "":
        return True
    
    slow = 0     
    for fast in range(len(t)):

        if s[slow] == t[fast]:
            slow += 1
            
        if slow == len(s):
            return True
    
    return False
    
    

class TestIsSubsequence(unittest.TestCase):
    
    
    def test_is_subsequence_1(self):
        
        self.assertEqual(isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(isSubsequence("ace", "abcde"), True)
        self.assertEqual(isSubsequence("axc", "ahbgdc"), False)
        self.assertEqual(isSubsequence("", "ahbgdc"), True)
        self.assertEqual(isSubsequence("a", "b"), False)
        
        

if __name__ == "__main__":
    unittest.main()