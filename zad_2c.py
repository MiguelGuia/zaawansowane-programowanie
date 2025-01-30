# c. Utwórz funkcję, która otrzyma w parametrze listę 10 licz
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
# Interpreter python, podstawowe operacje (zmienne, warunku, pętle, funkcje) 11
# jedynie parzyste elementy.

def even_list(list):
    for i in range(0, len(list), 2):
        print(list[i])

even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])