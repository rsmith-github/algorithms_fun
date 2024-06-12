# Solution

- loop through input array, comparing each character to previous character.
- if previous is equal to current character, count it.
- else add previous character string
- within the else, if count is not 1, add the count as well, according to the expected output.
- within the else, set previous character to current character and set count to 1, because there is now 1 new character.
- if at last character make sure to add it to the 'empty' string
- then again, if count is not 1, add it. (constraint in problem description)

- modify the input array, setting each character to the corresponding one in the string built
- remove all the extra elements
- return length of modified array

```python

def compress(chars):

    s = ''
    count = 0
    prev_char = chars[0]

    for i, current_char in enumerate(chars):

        if prev_char == current_char:
            count += 1
        else:
            s += prev_char

            if count != 1:
                s += str(count)

            prev_char = current_char

            count = 1

        if i == len(chars) - 1:
            s += current_char
            if count != 1:
                s += str(count)
    
    for i, ch in enumerate(list(s)):
        chars[i] = ch

    while len(chars) != len(s):
        chars.pop()

    return len(chars)

```

# Time Complexity

- Linear O(n)
