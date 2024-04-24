import unittest


def decode(message_file):

    # Create a map to contain each number and each word for each row
    words_map = {}

    # Open the file
    with open(message_file, 'r') as file:

        # Read line by line, splitting by " ".
        for line in file:
            split = line.strip().split(' ')
            # For each line insert the the numeric string converted to an integer, and the word as the value to the words_map dictionary.
            words_map[int(split[0])] = split[1]

    # Sort the keys in order, to respect the pyramid pattern.
    sorted_keys = sorted(words_map)

    # Create a "decoded" list of words, starting with the first word in 'words_map.' This will always be words_map[1] because the pyramid list is sorted.
    decoded = [words_map[1]]

    # Two iterators, starting from 2 and 3.
    i = 2
    j = 3

    # While i is less than or equal to the length of the keys, append the correct word according to the pyramid (Last element of each row)
    while i <= len(sorted_keys):

        # Append correct word. This is comes from the pattern 0,2,5,9,14,20,...
        decoded.append(words_map[i+1])
        i += j
        j += 1

    return " ".join(decoded)


# print(decode('python/decode/message.txt'))
# print(decode('python/decode/message2.txt'))
# print(decode('python/decode/message3.txt'))
# print(decode('python/decode/coding_qual_input.txt'))



class TestDecodeMessageFile(unittest.TestCase):

    def test_message_1(self):
        self.assertEqual(decode('python/decode/message.txt'),
                         "I love computers")

    def test_message_2(self):
        self.assertEqual(decode('python/decode/message2.txt'),
                         "you should go home")

    def test_message_3(self):
        self.assertEqual(decode('python/decode/message3.txt'),
                         "Today I will go to the mall")

    def test_message_qual_input(self):
        self.assertEqual(decode('python/decode/coding_qual_input.txt'),
                         "young system present student lot experiment strong crease sun company hurry remember milk us repeat clothe against meant history indicate pitch print bread would")


if __name__ == "__main__":
    unittest.main()

"""

       1
      2 3
     4 5 6
    7 8 9 10
  11 12 13 14 15
 16 17 18 19 20 21
22 23 24 25 26 27 28

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

0,2,5,9,14,20

"""
