'''
ONNX(Open Neural Network Exchange)，开放神经网络交换
是一种模型IR，用于在各种深度学习训练和推理框架转换的一个中间表示格式。
在实际业务中，可以使用Pytorch或者TensorFlow训练模型，
导出成ONNX格式，然后在转换成目标设备上支撑的模型格式
'''

from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('F:/yolo/ultralytics-main/datasets/Helmet/runs/detect/train/weights/best.pt')  # load a custom trained model

# Export the model
model.export(format='onnx')

'''
yolo export model=yolov8n.pt format=onnx  # export official model
yolo export model=path/to/best.pt format=onnx  # export custom trained model
'''