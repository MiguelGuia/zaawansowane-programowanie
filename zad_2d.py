#d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
#(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
#drugi element.

def every_second(list):
    for i in range(0, len(list), 2):
        print(list[i])
        
every_second([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])