'''Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jed
metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
ocen jest 50 w przeciwnym przypadku negatywną. Następnie należ
stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
zwracała true , a dla drugiego false .'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def is_passed(self):
        return sum(self.marks) / len(self.marks) >= 50


student1 = Student("Jan", [60, 70, 80])
student2 = Student("Anna", [30, 40, 45])

print(student1.name, "przeszedł?", student1.is_passed())
print(student2.name, "przeszedł?", student2.is_passed())