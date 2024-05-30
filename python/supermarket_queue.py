import unittest
import heapq


def queue_time(customers, n):

    tills = [0] * n
    
    for i in customers:
        tills[0] += i
        tills.sort()
        
    return max(tills)


class TestQueue(unittest.TestCase):

    def test_basic_examples(self):

        self.assertEqual(queue_time([], 1), 0,
                         "wrong answer for case with an empty queue")
        self.assertEqual(queue_time(
            [5], 1), 5, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time(
            [2], 5), 2, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([1, 2, 3, 4, 5], 1),
                         15, "wrong answer for a single till")
        self.assertEqual(queue_time(
            [1, 2, 3, 4, 5], 100), 5, "wrong answer for a case with a large number of tills")
        self.assertEqual(queue_time(
            [2, 2, 3, 3, 4, 4], 2), 9, "wrong answer for a case with two tills")


if __name__ == "__main__":
    unittest.main()
