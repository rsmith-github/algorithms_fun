import unittest


def count(s):

    result_object = {}

    # populate object based on string
    for char in s:
        keys = result_object.keys()
        if char not in keys and char.isalpha():
            result_object[char] = 1
        elif char.isalpha():
            result_object[char] += 1

    return result_object


class TestCount(unittest.TestCase):

    def setUp(self):
        self.input_1 = "abc"
        self.input_2 = "aabbcc"
        self.input_3 = "aabbc"

        # words and sentences
        self.canada = "canada"
        self.programming = "programming bootcamp"

    def test_basic_case(self):
        self.assertEquals({'a': 1, 'b': 1, 'c': 1}, count(self.input_1))

    def test_doubles(self):
        self.assertEquals({'a': 2, 'b': 2, 'c': 2}, count(self.input_2))

    def test_doubles_and_one_single(self):
        self.assertEquals({'a': 2, 'b': 2, 'c': 1}, count("aabbc"))

    def test_random_words_and_sentences(self):
        self.assertEquals({'c': 1, 'a': 3, 'n': 1, 'd': 1}, count(self.canada))
        self.assertEquals({'p': 2, 'r': 2, 'o': 3, 'g': 2, 'a': 2, 'm': 3,
                          'i': 1, 'n': 1, 'b': 1, 't': 1, 'c': 1}, count(self.programming))

    def test_empty(self):
        self.assertEqual({}, count(''))


if __name__ == '__main__':
    unittest.main()
