import unittest


def solution(number):

    # reference roman numbers
    r_number_reference = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    # roman number string to build
    roman_number = ""
    
    for key in sorted(r_number_reference.keys(), reverse=True):
        while number >= key:
            roman_number += r_number_reference[key]
            number -= key
            
    return roman_number


class TestSolution(unittest.TestCase):

    def test_given_examples(self):
        self.assertEqual(solution(1), 'I', "solution(1),'I'")
        self.assertEqual(solution(4), 'IV', "solution(4),'IV'")
        self.assertEqual(solution(6), 'VI', "solution(6),'VI'")
        self.assertEqual(solution(14), 'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21), 'XXI', "solution(21),'XXI'")
        self.assertEqual(solution(35), 'XXXV', "solution(35),'XXI'")
        self.assertEqual(solution(46), 'XLVI', "solution(46),'XLVI'")
        self.assertEqual(solution(89), 'LXXXIX', "solution(89),'LXXXIX'")
        self.assertEqual(solution(91), 'XCI', "solution(91),'XCI'")
        self.assertEqual(solution(984), 'CMLXXXIV', "solution(984),'CMLXXXIV'")
        self.assertEqual(solution(1000), 'M', 'solution(1000), M')
        self.assertEqual(solution(1889), 'MDCCCLXXXIX',
                         "solution(1889),'MDCCCLXXXIX'")
        self.assertEqual(solution(1989), 'MCMLXXXIX',
                         "solution(1989),'MCMLXXXIX'")


if __name__ == "__main__":
    unittest.main()

