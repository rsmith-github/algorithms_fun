# Solution

- split by whitespace string.split()
- reverse the string
- join with space

```python

def reverseWords(string: str) -> str:
    

    return ' '.join(reversed(string.split()))

```


# Time complexity

- Linear time O(n)