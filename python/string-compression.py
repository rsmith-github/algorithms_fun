import unittest

def compress(chars):
    # starting variables
    s = ''
    count = 0
    prev_char = chars[0] # previous character is the first character

    # loop through input array, comparing each character to previous character.
    for i, current_char in enumerate(chars):

        # if previous is equal to current character, count it.
        if prev_char == current_char:
            count += 1
        else: # else add previous character string
            s += prev_char
            
            # and if count is not 1, add the count as well, according to the expected output.
            if count != 1:
                s += str(count)

            # set previous character to current character
            prev_char = current_char
            
            # set count to 1, because there is now 1 new character.
            count = 1
        
        # if last at last character,
        if i == len(chars) - 1:

            # make sure to add it to the 'empty' string
            s += current_char
            
            # again, if count is not 1, add it. (constraint in problem description)
            if count != 1:
                s += str(count)
    
    # modify the input list
    for i, ch in enumerate(list(s)):
        chars[i] = ch

    # remove all the extra elements
    while len(chars) != len(s):
        chars.pop()

    # return length of modified array
    return len(chars)



class TestCompress(unittest.TestCase):
    
    def test_compress_basic(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = ["a", "2", "b", "2", "c", "3"]
        length = compress(chars)
        self.assertEqual(length, 6)
        self.assertEqual(chars[:length], expected)

    def test_compress_single(self):
        chars = ["a"]
        expected = ["a"]
        length = compress(chars)
        self.assertEqual(length, 1)
        self.assertEqual(chars[:length], expected)

    def test_compress_long_repeats(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        expected = ["a", "b", "1", "2"]
        length = compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], expected)

    def test_compress_no_repeats(self):
        chars = ["a", "b", "c", "d"]
        expected = ["a", "b", "c", "d"]
        length = compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], expected)

    def test_compress_mixed_characters(self):
        chars = ["a", "a", "b", "b", "c", "d", "d", "d"]
        expected = ["a", "2", "b", "2", "c", "d", "3"]
        length = compress(chars)
        self.assertEqual(length, 7)
        self.assertEqual(chars[:length], expected)

    def test_compress_large_counts(self):
        chars = ["a"] * 100
        expected = ["a", "1", "0", "0"]
        length = compress(chars)
        self.assertEqual(length, 4)
        self.assertEqual(chars[:length], expected)


if __name__ == "__main__":
    unittest.main()