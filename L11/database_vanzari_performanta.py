import pandas as pd
import matplotlib.pyplot as plt

data = {
    'data': pd.date_range(start='2025-01-01', periods=60, freq='D'),
    'venit': [round(1000 + i * 50 + (i % 10) * 100, 2) for i in range(60)],
    'profit': [round(200 + i * 20 + (i % 5) * 50, 2) for i in range(60)]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df['data'], df['venit'], label='Venit total', color='blue', marker='o')
plt.plot(df['data'], df['profit'], label='Profit total', color='green', marker='x')
plt.title('Evoluția veniturilor și profitului pe zile')
plt.xlabel('Ziua')
plt.ylabel('Valoare (RON)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

data_vanzari = {
    'data': pd.date_range(start='2025-01-01', periods=60, freq='D'),
    'pret': [round(50 + (i % 15) * 5, 2) for i in range(60)],
    'cantitate': [round(10 + (i % 7), 0) for i in range(60)]
}

df_vanzari = pd.DataFrame(data_vanzari)

plt.figure(figsize=(10, 6))
plt.hist(df_vanzari['pret'], bins=15, color='orange', edgecolor='black')
plt.title('Distribuția prețurilor')
plt.xlabel('Preț (RON)')
plt.ylabel('Frecvența')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df_vanzari['cantitate'], bins=10, color='purple', edgecolor='black')
plt.title('Distribuția cantităților vândute')
plt.xlabel('Cantitate')
plt.ylabel('Frecvența')
plt.grid(True)
plt.tight_layout()
plt.show()

data_promo = {
    'data': pd.date_range(start='2025-01-01', periods=60, freq='D'),
    'promo': [1 if i % 5 == 0 else 0 for i in range(60)],
    'pret': [round(50 + (i % 15) * 5, 2) for i in range(60)]
}

df_promo = pd.DataFrame(data_promo)

df_promo['pret_media'] = df_promo.groupby('promo')['pret'].transform('mean')

plt.figure(figsize=(10, 6))
plt.plot(df_promo['data'], df_promo['pret'], label='Prețuri vândute', color='blue')
plt.scatter(df_promo[df_promo['promo'] == 1]['data'], df_promo[df_promo['promo'] == 1]['pret'], color='red', label='Promoție activă')
plt.title('Impactul promoțiilor asupra prețurilor')
plt.xlabel('Ziua')
plt.ylabel('Preț (RON)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
