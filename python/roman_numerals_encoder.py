import unittest


def solution(number):

    # reference roman numbers
    r_number_reference = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        100: 'M',
    }

    # roman number string to build
    roman_number = ""
    
    # Separate by decimal

    if number < 5:
        pass
    elif number >= 5 and number < 10:
        pass
    elif number >= 10 and number < 50:
        pass
    elif number >= 50 and number < 100:
        pass
    elif number >= 100 and number < 500:
        pass
    elif number >= 500 and number < 1000:
        pass

            return
            
    


class TestSolution(unittest.TestCase):

    def test_given_examples(self):
        self.assertEqual(solution(1), 'I', "solution(1),'I'")
        self.assertEqual(solution(4), 'IV', "solution(4),'IV'")
        self.assertEqual(solution(6), 'VI', "solution(6),'VI'")
        self.assertEqual(solution(14), 'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21), 'XXI', "solution(21),'XXI'")
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
