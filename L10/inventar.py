class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self):
        name = input("Introduceți numele produsului: ")
        try:
            quantity = int(input("Introduceți cantitatea: "))
            if name in self.products:
                self.products[name] += quantity
            else:
                self.products[name] = quantity
            print(f"Produsul '{name}' a fost adăugat cu succes.")
        except ValueError:
            print("Eroare: Introduceți o cantitate validă!")
    def search_product(self):
        name = input("Introduceți numele produsului căutat: ")
        if name in self.products:
            print(f"Produsul găsit: {name} - Cantitate: {self.products[name]}")
        else:
            print("Eroare: Produsul nu există în inventar!")
    def update_quantity(self):
        name = input("Introduceți numele produsului: ")
        if name in self.products:
            try:
                quantity = int(input("Introduceți noua cantitate: "))
                self.products[name] = quantity
                print(f"Produsul '{name}' a fost actualizat cu succes.")
            except ValueError:
                print("Eroare: Introduceți o cantitate validă!")
        else:
            print("Eroare: Produsul nu există în inventar!")
    def display_inventory(self):
        print("Inventar curent:")
        for name, quantity in self.products.items():
            print(f"{name}: {quantity}")

inventory = Inventory()
while True:
    print("\n--- Sistem de gestionare a inventarului ---")
    print("1. Adaugă produs")
    print("2. Caută produs")
    print("3. Actualizează cantitatea unui produs")
    print("4. Afișează inventarul")
    print("5. Ieșire")
    choice = input("Alegeți o opțiune: ")
    if choice == "1":
        inventory.add_product()
    elif choice == "2":
        inventory.search_product()
    elif choice == "3":
        inventory.update_quantity()
    elif choice == "4":
        inventory.display_inventory()
    elif choice == "5":
        print("La revedere!")
        break
    else:
        print("Eroare: Opțiune invalidă!")