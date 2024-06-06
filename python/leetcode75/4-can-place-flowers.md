# Solution

- check first element is zero and element to right is zero
- check last element is zero and previous element is zero
- check all elements inbetween (prev, next and current elements are all 0)

```python

for i in range(len(flowerbed)):
    # last element
    if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
        n -= 1
    elif ( i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 ) or ( flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 ): # first element or in between
        n -= 1
        flowerbed[i] = 1 

return n <= 0

````



# Time Complexity

- Linear time O(n)