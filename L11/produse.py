import numpy as np
import pandas as pd

np.random.seed(42)

zile = [f"Zi_{i+1}" for i in range(60)]
produse = [f"Produs_{i+1}" for i in range(15)]

data = []

for zi in zile:
    numar_produse = np.random.randint(5, 16)
    produse_zi = np.random.choice(produse, numar_produse, replace=False)
    preturi_initiale = np.random.normal(40, 8, numar_produse).clip(10, 100)
    cantitati = np.random.randint(1, 11, numar_produse)
    promotii = np.random.choice([True, False], numar_produse, p=[0.3, 0.7])
    preturi_finale = np.where(promotii, preturi_initiale * 0.8, preturi_initiale)

    for produs, pret_init, cant, pret_final in zip(produse_zi, preturi_initiale, cantitati, preturi_finale):
        venit = pret_final * cant
        cost = pret_final * cant * 0.7
        profit = venit - cost
        data.append([zi, produs, pret_init, cant, pret_final, venit, cost, profit])

columns = ["Zi", "Produs", "Pret_initial", "Cantitate", "Pret_final", "Venit", "Cost", "Profit"]
df = pd.DataFrame(data, columns=columns)

vanzari_zilnice = df.groupby("Zi").agg(
    Total_Vanzari=("Venit", "sum"), Total_Profit=("Profit", "sum")
).reset_index()

statistici_generale = {
    "Preturi": {
        "Media": df["Pret_initial"].mean(),
        "Maxim": df["Pret_initial"].max(),
        "Minim": df["Pret_initial"].min(),
    },
    "Cantitati": {
        "Media": df["Cantitate"].mean(),
        "Maxim": df["Cantitate"].max(),
        "Minim": df["Cantitate"].min(),
    },
    "Profituri": {
        "Media": vanzari_zilnice["Total_Profit"].mean(),
        "Maxim": vanzari_zilnice["Total_Profit"].max(),
        "Minim": vanzari_zilnice["Total_Profit"].min(),
    },
    "Totaluri": {
        "Total_Vanzari": vanzari_zilnice["Total_Vanzari"].sum(),
        "Total_Profit": vanzari_zilnice["Total_Profit"].sum(),
    },
}

print("Exemple de date generate:")
print(df.head())

print("\nTotalurile zilnice:")
print(vanzari_zilnice.head())

print("\nStatistici generale:")
for categorie, valori in statistici_generale.items():
    print(categorie + ":", valori)
