from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)

model.train(data='Yolo_Tutorial/config.yaml', epochs=1, imgsz=640)
