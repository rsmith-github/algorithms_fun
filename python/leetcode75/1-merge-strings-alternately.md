# Solution

**Brute force, adding one letter at a time from each string to a new result list then joining in the end.**

``` python
def mergeAlternately(word1, word2):

    l1, l2 = len(word1), len(word2)
    res = []
    
    for i in range(0, max(l1, l2)):    
        # conditionals make sure we are in bounds in case different lengths
        if i < l1:
            res.append(word1[i])
        if i < l2:
            res.append(word2[i])
            
    return "".join(res)
```
or

``` python
def mergeAlternately(self, word1: str, word2: str) -> str:
    
    i, j = 0, 0
    r = []

    while i < len(word1) and j < len(word2):
        r.append(word1[i])
        r.append(word2[j]) 
        i, j = i + 1, j + 1

    r.append(word1[i:])
    r.append(word2[j:])
    return "".join(r)
```

# Time Complexity:

- Linar time or O(n)