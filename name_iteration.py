import os

def rename_images_in_folder(folder_path, base_filename):
    # Überprüfe, ob der Ordner existiert
    if not os.path.exists(folder_path):
        print(f"Der Ordner '{folder_path}' existiert nicht.")
        return

    # Hole alle gültigen Bild-Dateinamen und sortiere sie alphabetisch
    valid_images = sorted([f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png", ".gif"))])

    # Generiere die neuen Dateinamen
    new_names = [f"{base_filename}_{i+1}{os.path.splitext(img)[1]}" for i, img in enumerate(valid_images)]

    # Benennen Sie die Dateien um
    for old_name, new_name in zip(valid_images, new_names):
        old_filepath = os.path.join(folder_path, old_name)
        new_filepath = os.path.join(folder_path, new_name)
        os.rename(old_filepath, new_filepath)
        print(f"Datei umbenannt: {old_name} -> {new_name}")

if __name__ == "__main__":
    # Definiere den Ordnerpfad, die Basisbezeichnung
    folder_path ="großer_Baumdatensatz/images/train"
    base_filename = "apfel"

    # Ändere die Bezeichnung der Bilder im angegebenen Ordner
    rename_images_in_folder(folder_path, base_filename)
