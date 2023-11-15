from ultralytics import YOLO
import cv2
import numpy as np

model_path = 'YOLOv8_3500_Bäume/best.pt'
image_path = 'Aufnahmen_Realsense/saved_images/image_1.png'

# Bild laden und Größe ermitteln
img = cv2.imread(image_path)
H, W, _ = img.shape

# Modell laden
model = YOLO(model_path)

# Modell auf das Bild anwenden
results = model(img)

# Für das Übereinanderlegen vorbereiten
overlay_img = img.copy()

# Für jedes erkannte Objekt
for result in results:
    # Für jede Maske des erkannten Objekts
    for j, mask in enumerate(result.masks.data):
        # Maske in ein numpy-Array umwandeln und skalieren
        mask = mask.numpy() * 255
        mask = mask.astype(np.uint8)
        mask_resized = cv2.resize(mask, (W, H))

        # Maske unter einem eindeutigen Namen speichern
        output_path = f'./output_mask_{j}.png'
        cv2.imwrite(output_path, mask_resized)

        # Fenster für die Maske erstellen und Größe einstellen
        window_name = f'Maske {j}'
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, 800, 600)  # Fenstergröße auf 800x600 setzen

        # Maske anzeigen
        cv2.imshow(window_name, mask_resized)

        # Maske zum Übereinanderlegen vorbereiten
        colored_mask = cv2.applyColorMap(mask_resized, cv2.COLORMAP_JET)
        overlay_img = cv2.addWeighted(overlay_img, 1, colored_mask, 0.5, 0)

# Fenster für das Originalbild erstellen und Größe einstellen
cv2.namedWindow('Originalbild', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Originalbild', 800, 600)  # Fenstergröße auf 800x600 setzen
cv2.imshow('Originalbild', img)

# Fenster für das übereinandergelegte Bild erstellen und Größe einstellen
cv2.namedWindow('Uebereinandergelegtes Bild', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Uebereinandergelegtes Bild', 800, 600)  # Fenstergröße auf 800x600 setzen
cv2.imshow('Uebereinandergelegtes Bild', overlay_img)

# Warten, bis ein Tastendruck erfolgt
cv2.waitKey(0)
cv2.destroyAllWindows()
