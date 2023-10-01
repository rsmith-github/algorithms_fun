import unittest

def likes(list):
    if list == []:
        return "no one likes this"
    
    return ''.join(word + ' and ' if i < len(list)-1 else word for i,word in enumerate(list)) + ' like this'

class TestLikes(unittest.TestCase):

    def test_example_cases(self):
        self.assertEqual(likes([]), 'no one likes this')
        # self.assertEqual(likes(['Peter']), 'Peter likes this')
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
        
        

if __name__ == '__main__':
    unittest.main()