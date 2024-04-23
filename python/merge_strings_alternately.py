import unittest


def mergeAlternately(word1, word2):

    l1, l2 = len(word1), len(word2)
    res = []
    
    for i in range(0, max(l1, l2)):    
        # conditionals make sure we are in bounds in case different lengths
        if i < l1:
            res.append(word1[i])
        if i < l2:
            res.append(word2[i])
            
    return "".join(res)

class TestMergeAlternately(unittest.TestCase):

    def test_merge_alternately(self):
        self.assertEqual(mergeAlternately('abc', 'def'), 'adbecf')
        self.assertEqual(mergeAlternately('abc', 'pqr'), 'apbqcr')
        # self.assertEqual(mergeAlternately('ab', 'pqrs'), 'apbqrs')


if __name__ == "__main__":
    unittest.main()
