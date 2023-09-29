import unittest

def solution(string):
    
    result = ''
    
    for ch in string:
        if ch.isupper():
            result += " " + ch
            continue

        result += ch
    
    return result

class TestSolution(unittest.TestCase):
    
    def test_hello_world(self):
        self.assertEqual(solution("helloWorld"), "hello World")
        
    def test_camel_case(self):
        self.assertEqual(solution("camelCase"), "camel Case")
    
    def test_break_camel_case(self):
        self.assertEqual(solution("breakCamelCase"), "break Camel Case")

if __name__ == "__main__":
    unittest.main()
