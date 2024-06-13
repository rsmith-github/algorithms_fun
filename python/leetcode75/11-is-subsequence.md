# Solution

- set 'slow' pointer to 0
- iterate through longer string
- if t\[current\] (fast) pointer is equal to s\[slow\] pointer, increment 'slow' pointer
- if slow is equal to length of s, return True
- otherwise return False.

- at the start, if s is longer than t, return False instantly. This will help speed up some test cases.

# Time Complexity
- Linear O(n)