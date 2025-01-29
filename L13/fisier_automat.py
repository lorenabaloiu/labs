import os

def rename_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Directorul specificat nu există.")
        return
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            new_filename = f"renamed_{filename}"
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Redenumit: {filename} -> {new_filename}")

def main():
    folder_path = input("Introduceți calea către folderul dorit: ")
    rename_files_in_folder(folder_path)


if __name__ == "__main__":
    main()