'''6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typ
list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.'''

from typing import List

def merge_lists(list1: List, list2: List) -> List:
    return list((set(list1 + list2)**3))

print(merge_lists([1, 2, 3], [3, 4, 5]))