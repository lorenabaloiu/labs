def divide_numbers():
    try:
        a = float(input("Introduceți primul număr: "))
        b = float(input("Introduceți al doilea număr: "))
        result = a / b
        print(f"Rezultatul împărțirii este: {result}")
    except ZeroDivisionError:
        print("Eroare: Împărțirea la zero nu este permisă!")
    except ValueError:
        print("Eroare: Introduceți numere valide!")

divide_numbers()