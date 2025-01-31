'''5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a dru
typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
drugim.'''

def is_in_list(list_: list, number: int) -> bool:
    return number in list_

result = is_in_list([1, 2, 3], 2)
print(result)