import unittest
def solution(n):
    # TODO convert int to roman string
    return

class TestSolution(unittest.TestCase):
    
    def test_given_examples(self):    
        self.assertEqual(solution(1),'I', "solution(1),'I'")
        self.assertEqual(solution(4),'IV', "solution(4),'IV'")
        self.assertEqual(solution(6),'VI', "solution(6),'VI'")
        self.assertEqual(solution(14),'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21),'XXI', "solution(21),'XXI'")
        self.assertEqual(solution(89),'LXXXIX', "solution(89),'LXXXIX'")