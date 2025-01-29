import requests
from tabulate import tabulate

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea datelor: {e}")
        return []

def filter_users_by_city(users, city):
    return [user for user in users if user['address']['city'].lower() == city.lower()]

def display_users(users):
    if not users:
        print("Nu există utilizatori de afișat.")
        return
    table_data = []
    for user in users:
        table_data.append([
            user['id'], user['name'], user['username'], user['email'],
            user['address']['city'], user['company']['name'], user['phone'], user['website']
        ])
    headers = ["ID", "Nume", "Username", "Email", "Oraș", "Companie", "Telefon", "Website"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def main():
    users = fetch_users()
    if users:
        print("\nToți utilizatorii:")
        display_users(users)

        city = "Gwenborough"
        filtered_users = filter_users_by_city(users, city)
        print(f"\nUtilizatori din {city}:")
        display_users(filtered_users)

if __name__ == "__main__":
    main()
