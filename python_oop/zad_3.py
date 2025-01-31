'''Stworzyć następujące klas
Property (klasa opisująca posiadłość/nieruchomość), posiadająca
pola:
area
rooms (int)
price
address
House (klasa dziedzicząca klasę Property , która opisuje dom),
posiadająca pola:
plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie),
posiadająca pola:
floor
Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę
__str__ , która będzie opisywała obiekt.
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
tworzenia instancji klasy za pośrednictwem konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je
wyświetlić.'''

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Property: {self.address}\n"
                f"Area: {self.area} m²\n"
                f"Rooms: {self.rooms}\n"
                f"Price: {self.price} zł")


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House: {self.address}\n"
                f"Area: {self.area} m²\n"
                f"Rooms: {self.rooms}\n"
                f"Price: {self.price} zł\n"
                f"Plot size: {self.plot} m²")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat: {self.address}\n"
                f"Area: {self.area} m²\n"
                f"Rooms: {self.rooms}\n"
                f"Price: {self.price} zł\n"
                f"Floor: {self.floor}")

house = House(150, 5, 1200000, "Warszawska 3, Warszawa", 500)
flat = Flat(80, 3, 600000, "Krakowska 10, Krakow", 2)

print(house)
print("\n" + "=" * 50 + "\n")
print(flat)