import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [("Bitcoin", data["bitcoin"]["usd"]), ("Ethereum", data["ethereum"]["usd"])]
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea prețurilor criptomonedelor: {e}")
        return []

def get_crypto_news():
    url = "https://www.coindesk.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("a", class_="headline", limit=5)
        news = [(article.text.strip(), url + article["href"]) for article in articles]
        return news
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea știrilor: {e}")
        return []

def display_crypto_data():
    prices = get_crypto_prices()
    if prices:
        print("\nPrețurile criptomonedelor:")
        print(tabulate(prices, headers=["Criptomonedă", "Preț (USD)"], tablefmt="grid"))

def display_crypto_news():
    news = get_crypto_news()
    if news:
        print("\nCele mai recente 5 știri despre criptomonede:")
        for title, link in news:
            print(f"- {title}\n  {link}")

def main():
    display_crypto_data()
    display_crypto_news()

if __name__ == "__main__":
    main()