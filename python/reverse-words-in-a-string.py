import unittest


def reverseWords(string: str) -> str:
    
    string_split = string.split()
    string_split.reverse()
    
    return " ".join(string_split)

class TestReverseWords(unittest.TestCase):

    def test_reverse_vowels(self):

        self.assertEqual(reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(reverseWords('  hello world  '), 'world hello')
        self.assertEqual(reverseWords('a good   example'), 'example good a')


if __name__ == "__main__":
    unittest.main()
