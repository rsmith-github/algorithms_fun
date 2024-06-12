import unittest

def compress(chars):

    pass


class TestCompress(unittest.TestCase):
    
    def test_compress_basic(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = ["a", "2", "b", "2", "c", "3"]
        length = compress(chars)
        self.assertEqual(length, 6)
        self.assertEqual(chars[:length], expected)

    def test_compress_single(self):
        chars = ["a"]
        expected = ["a"]
        length = compress(chars)
        self.assertEqual(length, 1)
        self.assertEqual(chars[:length], expected)

    def test_compress_long_repeats(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        expected = ["a", "b", "1", "2"]
        length = compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], expected)

    def test_compress_no_repeats(self):
        chars = ["a", "b", "c", "d"]
        expected = ["a", "b", "c", "d"]
        length = compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], expected)

    def test_compress_mixed_characters(self):
        chars = ["a", "a", "b", "b", "c", "d", "d", "d"]
        expected = ["a", "2", "b", "2", "c", "d", "3"]
        length = compress(chars)
        self.assertEqual(length, 7)
        self.assertEqual(chars[:length], expected)

    def test_compress_large_counts(self):
        chars = ["a"] * 100
        expected = ["a", "1", "0", "0"]
        length = compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], expected)


if __name__ == "__main__":
    unittest.main()