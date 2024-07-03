import os

def remove_classes_from_txt_files(folder_path, classes_to_remove):
    # 获取labels文件夹中所有的txt文件
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    for txt_file in txt_files:
        with open(os.path.join(folder_path, txt_file), 'r') as f:
            lines = f.readlines()

        # 保留不包含指定类别的行
        new_lines = [line for line in lines if not should_remove_line(line, classes_to_remove)]

        # 覆盖原来的txt文件内容
        with open(os.path.join(folder_path, txt_file), 'w') as f:
            f.writelines(new_lines)


def should_remove_line(line, classes_to_remove):
    class_id = int(line.split()[0])
    return class_id in classes_to_remove


if __name__ == "__main__":
    dataset_labels_folder = "F:/yolo/ultralytics-main/datasets/Helmet/valid/labels"
    classes_to_remove = [1, 2, 3]
    remove_classes_from_txt_files(dataset_labels_folder, classes_to_remove)