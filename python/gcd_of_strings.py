import unittest


def gcdOfStrings(str1, str2):
    if str1 + str2 == str2 + str1:
        greatestCommonStrLen = gcd(len(str1), len(str2))
        return str1[:greatestCommonStrLen]
    return ""

def gcd(a, b):
    
    while b:
        a, b = b, a % b
        
    return a

class TestGcdOfStrings(unittest.TestCase):

    def test_basic_tests(self):
        self.assertEqual(gcdOfStrings("ABCABC", "ABC"), "ABC")
        self.assertEqual(gcdOfStrings("ABCDEF", "ABC"), "")
        self.assertEqual(gcdOfStrings("ABABAB", "ABAB"), "AB")
        self.assertEqual(gcdOfStrings("LEET", "CODE"), "")


if __name__ == "__main__":
    unittest.main()