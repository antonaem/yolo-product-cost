from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolov8m-oiv7.pt")
# model = YOLO("runs/detect/train8/weights/best.pt")
# model.export(format="tflite")
# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data='coco8.yaml', epochs=5, imgsz=100, batch=512)

# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model("labels-06.jpg")

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="labels-06-result.jpg")  # save to disk
    print(result)