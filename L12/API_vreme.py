import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t+%w"
    try:
        response = requests.get(url, verify=False)  # Ignoră erorile SSL
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.HTTPError:
        print("Eroare: Orașul nu a fost găsit sau API-ul nu este disponibil.")
    except requests.exceptions.RequestException as e:
        print(f"Eroare la conectarea la API: {e}")
    return None

def main():
    city = input("Introduceți numele orașului: ")
    weather_info = get_weather(city)
    if weather_info:
        print(f"Vremea pentru {city}: {weather_info}")
    else:
        print("Nu s-au putut obține informații despre vreme.")

if __name__ == "__main__":
    main()