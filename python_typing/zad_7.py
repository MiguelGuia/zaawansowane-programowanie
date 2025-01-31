import requests
import argparse

class Brewery:
    def __init__(self, id, name, brewery_type, street, city, state, postal_code, country, phone, website_url, updated_at):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at

    def __str__(self):
        return (f"Brewery: {self.name}\n"
                f"Type: {self.brewery_type}\n"
                f"Address: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}\n"
                f"Phone: {self.phone}\n"
                f"Website: {self.website_url}\n"
                f"Last Updated: {self.updated_at}\n")


def fetch_breweries(city=None, limit=20):
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": limit}
    if city:
        params["by_city"] = city
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


def create_brewery_objects(data):
    breweries = []
    for item in data:
        brewery = Brewery(
            id=item.get('id'),
            name=item.get('name'),
            brewery_type=item.get('brewery_type'),
            street=item.get('street'),
            city=item.get('city'),
            state=item.get('state'),
            postal_code=item.get('postal_code'),
            country=item.get('country'),
            phone=item.get('phone'),
            website_url=item.get('website_url'),
            updated_at=item.get('updated_at')
        )
        breweries.append(brewery)
    return breweries


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch breweries from Open Brewery DB.")
    parser.add_argument("--city", type=str, help="Filter breweries by city.")
    args = parser.parse_args()

    try:
        data = fetch_breweries(city=args.city, limit=20)
        breweries = create_brewery_objects(data)
        for brewery in breweries:
            print(brewery)
            print("=" * 50)
    except Exception as e:
        print(e)