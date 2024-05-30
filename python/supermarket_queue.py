import unittest

def queue_time(customers, n):
    
    # initialise virtual checkouts data structure
    checkouts = {f'checkout-{str(i+1)}': None for i in range(n)}
    
    # basic cases based on math
    if n == 1 or len(customers) == 1:
        return sum(customers)
    if n > sum(customers):
        return max(customers)
    
    # get first customer in line
    next_customer = customers.pop(0)
    
    # counts how much time has passed since last iteration (fastest customer to leave)
    counter = 0
    
    # loop through customers
    while len(customers):
        
        # send customers to tills (in order)
        for till, customer in checkouts.items():
            # if there is no customer in till, add the customer at front of line.
            if customer == None:
                checkouts[till] = next_customer
                break
        
        # get next customer
        next_customer = customers.pop(0)
        
        # if all tills are occupied
        if None not in checkouts.values():
            
            # keep track of who will complete their checkout first
            fastest = min(checkouts.values())
            
            # get key of till which will be vacant first
            fastest_key = list(checkouts.keys())[list(checkouts.values()).index(fastest)]
            
            # subtract fastest checkout time from other tills to keep track of time for everyone
            for key, _ in checkouts.items():
                checkouts[key] -= fastest
            
            # assign next customer to whichever till checked out first
            checkouts[fastest_key] = next_customer
            
            # update variable keeping track of how much time has passed
            counter += fastest
    
    # result will be all the fastest times plus whoever takes the longest in final group of customers
    return counter + checkouts[max(checkouts, key=checkouts.get)]



class TestQueue(unittest.TestCase):
        
    def test_basic_examples(self):
        

        self.assertEqual(queue_time([], 1), 0, "wrong answer for case with an empty queue")
        self.assertEqual(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
        self.assertEqual(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
        self.assertEqual(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")
        

if __name__ == "__main__":
    unittest.main()