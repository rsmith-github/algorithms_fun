# Solution

- Make sure that input strings concatenated in any order are equal to each other
- find greatest common divisor for length of each string
- return letters up to the greatest common divisor
- (implement gcd if necessary)

Python3
```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if (str1 + str2) == (str2 + str1):
            greatestCommStrLen = gcd(len(str1), len(str2))
            return str1[:greatestCommStrLen]
        
        return ""

```

Python2

```python
class Solution:

    def gcdOfStrings(self, str1, str2):
        
        if (str1 + str2) == (str2 + str1):
            greatestCommonStrLen = self.gcd(len(str1), len(str2))
            return str1[:greatestCommonStrLen]
        
        return ""

    def gcd(self, a, b):
        
        while b:
            a, b = b, a % b
        return a

```

Golang

```go

func gcdOfStrings(str1 string, str2 string) string {
	if str1 + str2 == str2 + str1 {
		var greatestCommStrLen int = gcd(len(str1), len(str2))
		return str1[:greatestCommStrLen]
	}
	return ""
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a % b
	}
	return a
}

```

# Time Complexity

Dominating term is the string concatenation and comparison

- Linear time O(m + n)