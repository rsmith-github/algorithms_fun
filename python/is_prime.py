import unittest


def is_prime(number):
    
    return False
    


class TestIsPrime(unittest.TestCase):
    
    def test_basic_tests(self):
        self.assertEqual(is_prime(0),  False, "0  is not prime")
        self.assertEqual(is_prime(1),  False, "1  is not prime")
        self.assertEqual(is_prime(2),  True, "2  is prime")
        self.assertEqual(is_prime(73), True, "73 is prime")
        self.assertEqual(is_prime(75), False, "75 is not prime")
        self.assertEqual(is_prime(-1), False, "-1 is not prime")