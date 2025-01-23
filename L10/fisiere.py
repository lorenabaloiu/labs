def sum_numbers_from_file():
    file_name = "numere.txt"
    try:
        with open(file_name, 'r') as file:
            numbers = file.readlines()
        total = 0
        for line in numbers:
            try:
                total += float(line.strip())
            except ValueError:
                print(f"Valoare invalidă găsită: {line.strip()}")
        print(f"Suma totală a numerelor din fișier este: {total}")
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{file_name}' nu există!")
    except IOError:
        print(f"Eroare: Nu s-a putut citi fișierul '{file_name}'!")

open("numere.txt", "a").close()
sum_numbers_from_file()