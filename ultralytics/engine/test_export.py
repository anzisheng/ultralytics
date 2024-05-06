import torch

from ultralytics import YOLO

# Load a model
#
#model = YOLO('cross-hands.pt')
model = YOLO('yolov8n.pt')

model.export(format='torchscript')
#torch.save(model, "yolo8n.torchscript")