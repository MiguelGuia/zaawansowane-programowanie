'''7. Stworzyć skrypt pythonowy, który połączy się z API, które zawiera informac
o browarach (dokumentacja https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę
Brewery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
odpowiednim typowaniem.
W klasie należy zaimplementować magiczną metodę
__str__ która będzie opisywała dane przechowywane w obiekcie.
Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
utworzyć listę 20 instancji klasy
Brewery , którą przeiteruje i wyświetli każdy obiekt z osobna.

8. Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city , który mo
być przekazywany w wierszu poleceń podczas wykonywania (np. python
main.py --city=Berlin ). Należy wykorzystać moduł argparse do wczytywania
przekazywanych parametrów, a w razie przekazania wartości ograniczyć
pobierane browary do miasta, które zostało wskazane.'''

import argparse
import requests

class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: str,
        address_2: str,
        address_3: str,
        city: str,
        county_province: str,
        state: str,
        postal_code: str,
        country: str,
        longitude: str,
        latitude: str,
        phone: str,
        website_url: str,
        updated_at: str,
        created_at: str,
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.county_province = county_province
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        return (
            f"Brewery(\n"
            f"  id={self.id},\n"
            f"  name={self.name},\n"
            f"  brewery_type={self.brewery_type},\n"
            f"  street={self.street},\n"
            f"  city={self.city},\n"
            f"  state={self.state},\n"
            f"  country={self.country},\n"
            f"  website_url={self.website_url},\n"
            f")\n"
        )

def main():
    
    parser = argparse.ArgumentParser(
        description="Skrypt pobierający informacje o browarach z OpenBreweryDB."
    )
    
    parser.add_argument(
        "--city",
        type=str,
        required=False,
        help="Nazwa miasta, z którego mają być pobrane browary (np. Berlin).",
    )
    args = parser.parse_args()

    url = "https://api.openbrewerydb.org/breweries"
    params = {
        "per_page": 20,  
    }

    if args.city:
        params["by_city"] = args.city

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    
    breweries = []
    for brewery_data in data:
        
        brewery = Brewery(
            id=brewery_data.get("id", ""),
            name=brewery_data.get("name", ""),
            brewery_type=brewery_data.get("brewery_type", ""),
            street=brewery_data.get("street", ""),
            address_2=brewery_data.get("address_2", ""),
            address_3=brewery_data.get("address_3", ""),
            city=brewery_data.get("city", ""),
            county_province=brewery_data.get("county_province", ""),
            state=brewery_data.get("state", ""),
            postal_code=brewery_data.get("postal_code", ""),
            country=brewery_data.get("country", ""),
            longitude=brewery_data.get("longitude", ""),
            latitude=brewery_data.get("latitude", ""),
            phone=brewery_data.get("phone", ""),
            website_url=brewery_data.get("website_url", ""),
            updated_at=brewery_data.get("updated_at", ""),
            created_at=brewery_data.get("created_at", ""),
        )
        breweries.append(brewery)

    
    for b in breweries:
        print(b)

if __name__ == "__main__":
    main()
