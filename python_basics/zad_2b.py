#b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą
#dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
#zwróci. Zadanie należy wykonać w 2 wersjach:
#i. Wykorzystując pętle for
#ii. Wykorzystując listę składaną

def multiply_list(list):
    for i in range(len(list)):
        list[i] *= 2
    return list

print(multiply_list([1, 2, 3, 4, 5]))