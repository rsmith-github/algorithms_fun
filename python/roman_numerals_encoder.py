import unittest


def solution(number):

    # reference roman numbers
    r_number_reference = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        100: 'M',
    }

    # roman number string to build
    roman_number = ""

    # Separate by range

    if number <= 10:
        return r_number_reference[number]
    elif number >= 10 and number < 50:
        # separate digits
        digits = get_digits(number)
        
        # reverse order for convenience
        digits.reverse()
        
        # add 10 for each 10 in number
        for _ in range(0, digits[0]):
            roman_number += r_number_reference[10]
            
        # add single digit
        roman_number += r_number_reference[digits[1]]
        
        return roman_number

    elif number >= 50 and number < 100:
        pass
    elif number >= 100 and number < 500:
        pass
    elif number >= 500 and number < 1000:
        pass

    return roman_number


def get_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = int(number / 10)
    return digits


class TestSolution(unittest.TestCase):

    def test_given_examples(self):
        self.assertEqual(solution(1), 'I', "solution(1),'I'")
        self.assertEqual(solution(4), 'IV', "solution(4),'IV'")
        self.assertEqual(solution(6), 'VI', "solution(6),'VI'")
        self.assertEqual(solution(14), 'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21), 'XXI', "solution(21),'XXI'")
        self.assertEqual(solution(35), 'XXXV', "solution(35),'XXI'")
        self.assertEqual(solution(89), 'LXXXIX', "solution(89),'LXXXIX'")
        self.assertEqual(solution(91), 'XCI', "solution(91),'XCI'")
        self.assertEqual(solution(984), 'CMLXXXIV', "solution(984),'CMLXXXIV'")
        self.assertEqual(solution(1000), 'M', 'solution(1000), M')
        self.assertEqual(solution(1889), 'MDCCCLXXXIX',
                         "solution(1889),'MDCCCLXXXIX'")
        self.assertEqual(solution(1989), 'MCMLXXXIX',
                         "solution(1989),'MCMLXXXIX'")


# if __name__ == "__main__":
#     unittest.main()

solution(21)
