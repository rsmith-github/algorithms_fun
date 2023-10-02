import unittest

def likes(names):
    if names == []:
        return "no one likes this"

    length = len(names)
    
    if length == 1:
        return f'{names[0]} likes this'
    
    if length == 2:
        return f'{names[0]} and {names[1]} like this' 
    
    if length > 3:
        return f'{names[0]}, {names[1]} and {length - 2} others like this'
    
    # 3 names
    return f'{names[0]}, {names[1]} and {names[2]} like this'

class TestLikes(unittest.TestCase):

    def test_example_cases(self):
        self.assertEqual(likes([]), 'no one likes this')
        self.assertEqual(likes(['Peter']), 'Peter likes this')
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
        
        

if __name__ == '__main__':
    unittest.main()