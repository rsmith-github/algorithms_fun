import unittest


def gcdOfStrings(str1, str2):
    
    if len(str1) < len(str2):
        return gcdOfStrings(str2, str1)
    if str1 == str2:
        return str1
    if str1.startswith(str2):
        return gcdOfStrings(str1[len(str2):], str2)
    return ""

class TestGcdOfStrings(unittest.TestCase):

    def test_basic_tests(self):
        self.assertEqual(gcdOfStrings("ABCABC", "ABC"), "ABC")
        self.assertEqual(gcdOfStrings("ABCDEF", "ABC"), "")
        self.assertEqual(gcdOfStrings("ABABAB", "ABAB"), "AB")
        self.assertEqual(gcdOfStrings("LEET", "CODE"), "")


if __name__ == "__main__":
    unittest.main()