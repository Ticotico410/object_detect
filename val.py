from ultralytics import YOLO

if __name__=='__main__':
    # Load a model
    # model = YOLO('yolov8s.pt')  # load an official model
    model = YOLO('F:/Datasets_project/runs/detect/train/weights/best.pt')  # load a custom model

    # Validate the model
    metrics = model.val()  # no arguments needed, dataset and settings remembered
    metrics.box.map    # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps   # a list contains map50-95 of each category
# CLI expression
'''
yolo detect val model=yolov8n.pt  # val official model
yolo detect val model=path/to/best.pt  # val custom model

test code:
yolo task=detect mode=test model='F:/Datasets_project/runs/detect/train/weights/best.pt' data=data.yaml batch=16
'''
