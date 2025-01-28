import pandas as pd

fisier_csv = "vanzari_companie.csv"
df = pd.read_csv(fisier_csv)

df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df = df.dropna(subset=['Data'])

df['Luna'] = df['Data'].dt.month
df['An'] = df['Data'].dt.year

cele_mai_vandute_pe_luna = df.groupby(['An', 'Luna', 'Produs'])['Cantitate'].sum().reset_index()
cele_mai_vandute_pe_luna = cele_mai_vandute_pe_luna.sort_values(['An', 'Luna', 'Cantitate'], ascending=[True, True, False])

df['Venit'] = df['Cantitate'] * df['Pret']
venitul_total_pe_produs = df.groupby('Produs')['Venit'].sum().reset_index().sort_values('Venit', ascending=False)

start_date = pd.to_datetime("2024-01-01")
end_date = pd.to_datetime("2024-03-31")
interval_vanzari = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]

venit_mediu_lunar = df.groupby(['An', 'Luna'])['Venit'].mean().reset_index()

print("Cele mai vândute produse pe lună:")
print(cele_mai_vandute_pe_luna)

print("\nVenitul total pe fiecare produs:")
print(venitul_total_pe_produs)

print("\nVânzările între 01.01.2024 și 31.03.2024:")
print(interval_vanzari)

print("\nVenitul mediu lunar:")
print(venit_mediu_lunar)
