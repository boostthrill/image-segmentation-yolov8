import shutil
import os
import glob

# Pfad des Quellordners, von dem kopiert wird
source_folder = 'Stammdatensatz/seg/val'
# Pfad des Zielordners, in den kopiert wird
destination_folder = 'Datensatz_Tree_Branch_Stamm/labels/val'

# Erstellt den Zielordner, falls er nicht existiert
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Kopiert alle Dateien vom Quellordner in den Zielordner
# Hier wird angenommen, dass Sie alle Dateien kopieren möchten
# Wenn Sie nur Bilder kopieren möchten, ändern Sie den Dateityp entsprechend
for file_path in glob.glob(source_folder + '/*'):
    # Kopiert jede Datei einzeln
    shutil.copy(file_path, destination_folder)
