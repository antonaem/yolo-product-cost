from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
# model = YOLO("yolov8m-oiv7.pt")
model = YOLO("runs/detect/train2/weights/best.pt")
#
# Train the model on the COCO8 example dataset for 100 epochs
# results = model.train(data='coco8.yaml', epochs=10, imgsz=512)
#
# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model("123.jpg")

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
    print(result)