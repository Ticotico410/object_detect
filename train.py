from ultralytics import YOLO

if __name__ == '__main__':

    # model = YOLO('yolov8n.yaml')  # build a new model from YAML
    model = YOLO('F:/Datasets_project/runs/detect/dataset1_100epoch_n/train/weights/last.pt')
    # model = YOLO('yolov8n.pt')
    results = model.train(data="data.yaml", imgsz=640, epochs=30 , batch=8, device=0, workers=4, patience=0)

# CLI expression
'''
# Build a new model from YAML and start training from scratch
yolo detect train data=coco128.yaml model=yolov8n.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo detect train data=coco128.yaml model=yolov8n.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo detect train data=coco128.yaml model=yolov8n.yaml pretrained=yolov8n.pt epochs=100 imgsz=640
'''
