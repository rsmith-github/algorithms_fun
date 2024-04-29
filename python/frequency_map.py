

n = 54321

frequency_map = {}

while n > 0:
    digit = n % 10
    n = int(n/10)

    if not digit in frequency_map.keys():
        frequency_map[digit] = 1
    else:
        frequency_map[digit] += 1


print(frequency_map)