import csv


def process_csv(input_file, output_file):
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile, \
                open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

            reader = csv.DictReader(infile)
            fieldnames = ['Produs', 'Cantitate', 'Pret unitar', 'Valoare totala']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                try:
                    cantitate = int(row['Cantitate'])
                    pret_unitar = float(row['Pret unitar'])
                    valoare_totala = cantitate * pret_unitar

                    row['Valoare totala'] = round(valoare_totala, 2)
                    writer.writerow(row)
                except ValueError:
                    print(f"Eroare la procesarea liniei: {row}")
        print(f"Fișierul procesat a fost salvat ca '{output_file}'")
    except FileNotFoundError:
        print("Fișierul de intrare nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")


def main():
    input_file = input("Introduceți numele fișierului CSV de intrare: ")
    output_file = "procesat_" + input_file
    process_csv(input_file, output_file)


if __name__ == "__main__":
    main()