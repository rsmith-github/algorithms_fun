# Solution

- get current max (kid with most candies)
- compare to each index in the candies, after adding the extra candies that I have.
- return completed list

```python

def kids_with_candies(candies, extraCandies):
    
    current_max = max(candies)
    bool_list = []
    
    for candy_count in candies:
        if candy_count + extraCandies >= current_max:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list

```

# Time Complexity

Linear O(n)