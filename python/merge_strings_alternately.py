import unittest


def mergeAlternately(word1, word2):

    return ""


class TestMergeAlternately(unittest.TestCase):

    def test_merge_alternately(self):
        self.assertEqual(mergeAlternately('abc', 'def'), 'adbecf')
        self.assertEqual(mergeAlternately('abc', 'pqr'), 'apbqcr')


if __name__ == "__main__":
    unittest.main()
