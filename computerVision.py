from ultralytics import YOLO



# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Perform object detection on an image using the model
results = model('https://ultralytics.com/images/bus.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')