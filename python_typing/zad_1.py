'''1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname ,
następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie
go wyświetlić ( print )'''

def hello(name: str, surname: str) -> str:
    return f'Cześć {name} {surname}!'

result = hello('Jan', 'Kowalski')
print(result)
