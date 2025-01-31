'''4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy su
dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
informację jako typ logiczny bool'''

def is_greater_or_equal(a: int, b: int, c: int) -> bool:
    return a >= c and b >= c

result = is_greater_or_equal(2, 3, 1)
print(result)

result = is_greater_or_equal(2, 3, 4)
print(result)
