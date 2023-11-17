import shutil
import os

def move_files(source_folder, destination_folder, start_index, end_index):
    """
    Verschiebt Dateien von source_folder nach destination_folder.
    Die Dateien sollten durchnummeriert sein und im Format 'file1', 'file2', etc. vorliegen.
    """
    # Erstellt den Zielordner, falls er nicht existiert
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Durchläuft die angegebenen Indizes und verschiebt jede Datei
    for i in range(start_index, end_index + 1):
        file_name = f"tree_{i}.txt"  # Ersetzen Sie dies mit Ihrem Dateinamensschema
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Verschiebt die Datei, wenn sie existiert
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print(f"Datei {file_name} existiert nicht in {source_folder}")

# Pfad des Quellordners, von dem verschoben wird
source_folder = 'großer_Baumdatensatz/seg/train'

# Pfad des Zielordners, in den verschoben wird
destination_folder = 'großer_Baumdatensatz/seg/val'

# Start- und Endindex der zu verschiebenden Dateien
start_index = 3160
end_index = 3950

move_files(source_folder, destination_folder, start_index, end_index)
