import unittest


def filter_list(l):
    'return a new list with the strings filtered out'
    return [element for element in l if type(element) == int]


class FilterListTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_example_cases(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2])
        self.assertEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
        self.assertEqual(filter_list(
            [1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])
        
        

if __name__ == '__main__':
    unittest.main()