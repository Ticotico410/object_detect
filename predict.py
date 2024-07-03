from ultralytics import YOLO

if __name__=='__main__':
    # Load a model
    model = YOLO('F:/Datasets_project/runs/detect/TEST1_30epoch_dataset1_100epoch_best/train/weights/last.pt') # build a new model from scratch

    # Define path to the image file
    source = ('F:/Datasets_project/predict_data/images')
    # Run inference on the source
    results = model(source, save=True)  # list of Results objects
