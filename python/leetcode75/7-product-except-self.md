# Solution

- get prefix array
- get suffix (postfix) array
- multiply each position of result array by previous index of the prefix array and next index of the suffix array


Logic of prefix/postfix:
```
prefix:
->
|       a       |   a*b   | a*b*c | a*b*c*d |
postfix:
<-
| a*b*c*d | b*c*d |   c*d   |      d        |

the result is a multiply without the symbol in own position (the left value from prefix and the right one from postfix):
|    b*c*d  | a*c*d | a*b*d |   a*b*c   |
```


Python:
```python

def productExceptSelf(nums):
    
    # declare variables
    prefix = []
    suffix = []
    
    result = []
    
    # get prefix array
    left = 1
    for num in nums:
        left *= num
        prefix.append(left)
    
    # get suffix array
    right = 1
    for i in range(len(nums)-1, -1, -1):
        right *= nums[i]
        suffix.append(right)
    
    suffix.reverse()
    
    
    # multiply each position by previous index of the prefix array and next index of the suffix array
    for i in range(len(nums)):
        if i == 0:
            res_num = 1 * suffix[i+1]
        elif i == len(nums) - 1:
            res_num = 1 * prefix[i-1]
        else:
            res_num = suffix[i+1] * prefix[i-1]
            
        result.append(res_num)

    return result
    
    
```




# Time Complexity

- Linear O(n)