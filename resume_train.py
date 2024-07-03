from ultralytics import YOLO

# Resume interrupted trainings
if __name__ == '__main__':
    # Load a model
    model = YOLO('F:/Datasets_project/runs/detect/train3/weights/last.pt')  # load a partially trained model

    # Resume training
    results = model.train(resume=True)

'''
# Resume an interrupted training
yolo train resume model=path/to/last.pt
'''