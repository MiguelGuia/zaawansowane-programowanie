'''Stworzyć następujące klas
Library (klasa opisująca bibliotekę), posiadająca pola:
city
street
zip_code
open_hours (str)
phone
Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
first_name
last_name
hire_date
birth_date
city
street
zip_code
phone
Book (klasa opisująca książkę), posiadająca pola
library
publication_date
author_name
author_surname
number_of_pages
Order (klasa opisująca zamówienie), posiadająca pola:
employee
student
books (lista obiektów klasy Book)
order_date
Dodatkowo:
Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie
opisywała obiekt oraz ewentualne obiekty znajdujące się w tym obiekcie
(np. obiekt Library w obiekcie Book).
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
tworzenia instancji klasy za pośrednictwem konstruktora.
Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników,
studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )'''


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library: {self.street}, {self.city}, {self.zip_code}\n"
                f"Open Hours: {self.open_hours}\n"
                f"Phone: {self.phone}")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}\n"
                f"Hire Date: {self.hire_date}\n"
                f"Birth Date: {self.birth_date}\n"
                f"Address: {self.street}, {self.city}, {self.zip_code}\n"
                f"Phone: {self.phone}")


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book: {self.author_name} {self.author_surname}\n"
                f"Publication Date: {self.publication_date}\n"
                f"Pages: {self.number_of_pages}\n"
                f"Library: {self.library.street}, {self.library.city}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join([str(book) for book in self.books])
        return (f"Order Date: {self.order_date}\n"
                f"Employee: {self.employee.first_name} {self.employee.last_name}\n"
                f"Student: {self.student}\n"
                f"Books:\n{books_str}")

library1 = Library("Warsaw", "Main Street 1", "00-001", "9:00-17:00", "+48 123 456 789")
library2 = Library("Krakow", "Old Town 5", "30-002", "10:00-18:00", "+48 987 654 321")

employee1 = Employee("John", "Doe", "2020-01-15", "1985-05-10", "Warsaw", "Library Lane 2", "00-002", "+48 111 222 333")
employee2 = Employee("Jane", "Smith", "2019-03-20", "1990-08-25", "Krakow", "Book Street 3", "30-003", "+48 444 555 666")
employee3 = Employee("Alice", "Johnson", "2021-07-10", "1988-12-30", "Warsaw", "Reading Ave 4", "00-003", "+48 777 888 999")

book1 = Book(library1, "2005-04-01", "George", "Orwell", 328)
book2 = Book(library1, "1997-06-26", "J.K.", "Rowling", 309)
book3 = Book(library2, "1813-01-28", "Jane", "Austen", 432)
book4 = Book(library2, "1869-01-01", "Leo", "Tolstoy", 1225)
book5 = Book(library1, "1949-06-08", "George", "Orwell", 328)

order1 = Order(employee1, "Student1", [book1, book2], "2023-10-01")
order2 = Order(employee2, "Student2", [book3, book4, book5], "2023-10-02")

print(order1)
print("\n" + "="*50 + "\n")
print(order2)