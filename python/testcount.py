import unittest


def count(s):
    
    result_object = {}
    
    # populate object based on string
    for char in s:
        keys = result_object.keys()
        if char not in keys:
            result_object[char] = 1
        else:
            result_object[char] += 1
        
    return result_object


class TestCount(unittest.TestCase):
    
    def setUp(self):
        self.input_1 = "abc"
        self.input_2 = "aabbcc"

    def test_basic_case(self):
        self.assertEquals({'a': 1, 'b': 1, 'c': 1}, count("abc"))

    def test_doubles(self):
        self.assertEquals({'a': 2, 'b': 2, 'c': 2}, count("aabbcc"))

    def test_doubles_and_one_single(self):
        self.assertEquals({'a': 2, 'b': 2, 'c': 1}, count("aabbc"))
        
    def test_empty(self):
        self.assertEqual({}, count(''))


if __name__ == '__main__':
    unittest.main()