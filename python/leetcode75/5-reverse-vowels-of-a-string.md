# Solution

- two pointer
- swap place of each vowel if left and right are both vowels

more efficient solution
```python
def reverseVowels(s: str) -> str:

    vowels = "aeiouAEIOU"
    s_as_list = list(s)
    left = 0
    right = len(s) - 1
    
    while left < right:
        
        if s_as_list[left] not in vowels:
            left += 1
        if s_as_list[right] not in vowels:
            right -= 1
            
        if s_as_list[left] in vowels and s_as_list[right] in vowels:
            s_as_list[left], s_as_list[right] = s_as_list[right], s_as_list[left]
            left += 1
            right -= 1
        
    return "".join(s_as_list)


```

or

```python

    def reverseVowels(self, s: str) -> str:
        vowels = {"A":'a', "E": "e", "I": 'i', "O": "o", "U": "u"}
        new_string = ""
        vowels_in_string = []
        for letter in s:
            if letter.upper() in vowels:
                vowels_in_string.append(letter)
                new_string += "*"
            else:
                new_string += letter
        
        result = ""
        count = 0
        for letter in new_string:
            if letter == "*":
                count += 1
                result += vowels_in_string[len(vowels_in_string) - count]
            else:
                result += letter

        return result

```

# Time complexity
- Linear time O(n)