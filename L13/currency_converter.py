import requests

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["rates"]
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea cursurilor de schimb: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Moneda specificată nu este disponibilă.")
        return None
    rate = rates[to_currency] / rates[from_currency]
    converted_amount = amount * rate
    return converted_amount, rate

def main():
    rates = get_exchange_rates()
    if not rates:
        return
    from_currency = input("Introduceți moneda de proveniență (ex: USD, EUR, RON): ").upper()
    to_currency = input("Introduceți moneda de destinație (ex: USD, EUR, RON): ").upper()
    try:
        amount = float(input("Introduceți suma de convertit: "))
    except ValueError:
        print("Suma introdusă nu este validă.")
        return
    result = convert_currency(amount, from_currency, to_currency, rates)
    if result:
        converted_amount, rate = result
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (Curs: {rate:.4f})")

if __name__ == "__main__":
    main()
