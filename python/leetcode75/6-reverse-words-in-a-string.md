# Solution

- split by whitespace string.split()
- reverse the string
- join with space

```python

def reverseWords(string: str) -> str:
    
    string_split = string.split()
    string_split.reverse()
    
    return ' '.join(string_split)

```


# Time complexity

- Linear time O(n)