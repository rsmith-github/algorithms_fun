import unittest


def reverseVowels(s: str) -> str:
    
    pass


class TestReverseVowels(unittest.TestCase):
    
    
    def test_reverse_vowels(self):
        
        self.assertEqual(reverseVowels('hello'), 'holle')
        self.assertEqual(reverseVowels('leetcode'), 'leotcede')
        
        
        



if __name__ == "__main__":
    unittest.main()