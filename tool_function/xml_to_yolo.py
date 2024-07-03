import os
from os import listdir, getcwd
import re

classes = []  # 列表，储存标签类别
classes_dict = {}  # 字典，储存标签类别及对应的序号，yolo标签文件中用序号表示各个类别


def convert(Imgsize, box):
    width, height = Imgsize
    xmin, ymin, xmax, ymax = box
    dw = max(xmin, xmax) - min(xmin, xmax)  # 框的宽
    dh = max(ymin, ymax) - min(ymin, ymax)  # 框的高
    x_ = (xmin + xmax) / 2.0  # 框的中心点x坐标
    y_ = (ymin + ymax) / 2.0  # 框的中心点y坐标

    # 归一化
    cx = round(x_ / width, 6)
    cy = round(y_ / height, 6)
    w = round(dw / width, 6)
    h = round(dh / height, 6)

    return [cx, cy, w, h]


def save_txt(namepath, text):  # 将内容保存至文本文件中，即成功转化为yolo的标签文件
    with open(namepath, 'w') as f:
        f.write(text)


def convert_annotation(xml_path, name):
    xml_name = xml_path + "/" + name
    with open(xml_name, "r", encoding="utf-8") as f1:
        text = f1.read().replace("\n", "")
        text = text.replace(" ", "")
    # print(text)
    img_size = re.findall("<width>([0-9]+)</width>.*?<height>([0-9]+)</height>", text)[0]
    print(img_size)
    find_datas = re.findall(
        "<object>.*?<name>([a-z|A-Z]*?)</name>.*?<xmin>([0-9]+?)</xmin>.*?<ymin>([0-9]+?)</ymin>.*?<xmax>([0-9]+?)</xmax>.*?<ymax>([0-9]+?)</ymax>",
        text)
    # print(find_datas)
    savetext = ""
    for item in find_datas:  # 由于每张图片中可能存在多个类别或标签，将同张图片中所有标签内容保存在一个txt文件中
        class_ = item[0]  # 类别名
        if class_ not in classes:  # 判断此类别是否已存在于classes列表中
            classes.append(class_)  # 如果不存在，则添加至列表中
            classes_dict[class_] = len(classes) - 1  # 同时，为此类别标记序号，即第几个类别，从0开始标号

        print(item)
        imgsize = [int(img_size[0]), int(img_size[1])]  # 正则获取的内容为文本格式，需要转化为数字
        box = [int(item[1]), int(item[2]), int(item[3]), int(item[4])]
        site = convert(imgsize, box)  # 整理内容，归一化数值
        # print(class_,site)
        savetext += "{0} {1} {2} {3} {4}".format(classes_dict[class_], site[0], site[1], site[2], site[3])  # 按格式拼接内容
        savetext += "\n"  # 文本换行
    # print(savetext)
    name = name.split(".")[0]  # 获取文件名，不包含文件后缀
    save_txt(labels_p + "/" + name + ".txt", savetext.strip())  # 保存标签文件


if __name__ == "__main__":
    # root_path = os.getcwd()  # 获取当前目录绝对路径
    # print(root_path)
    labels_p = "F:\Datasets_project\datasets/roof/roof_original\labels"  # 定义标签储存的文件夹路径
    try:
        os.makedirs(labels_p)  # 创建文件夹
    except:
        pass
    xml_path = "F:\Datasets_project\datasets/roof/roof_original\labels_xml"  # .xml文件的父级文件夹路径
    xml_list = sorted(listdir(xml_path))  # 获取所有.xml文件名，并保存至列表中，同时排序
    print(xml_list[:20])  # 打印前20个内容，查看结果，验证是否正确
    for name in xml_list:  # 历遍列表
        print(name)
        convert_annotation(xml_path, name)  # 开始转化

    # print(classes, classes_dict)
    # with open(labels_p + "/classes.txt", "w") as f2:  # 保存类别标签文件
    #     text = ""
    #     for t in classes:
    #         text += t
    #         text += "\n"
    #     print(text)
    #     f2.write(text)
