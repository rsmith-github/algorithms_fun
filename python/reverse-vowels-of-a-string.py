import unittest


def reverseVowels(s: str) -> str:

    vowels = "aeiouAEIOU"
    s_as_list = list(s)
    left = 0
    right = len(s) - 1
    
    while left < right:
        
        if s_as_list[left] not in vowels:
            left += 1
        if s_as_list[right] not in vowels:
            right -= 1
            
        if s_as_list[left] in vowels and s_as_list[right] in vowels:
            s_as_list[left], s_as_list[right] = s_as_list[right], s_as_list[left]
            left += 1
            right -= 1
        
    return "".join(s_as_list)


class TestReverseVowels(unittest.TestCase):

    def test_reverse_vowels(self):

        self.assertEqual(reverseVowels('hello'), 'holle')
        self.assertEqual(reverseVowels('leetcode'), 'leotcede')


if __name__ == "__main__":
    unittest.main()
