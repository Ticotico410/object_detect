import os
import fileinput

# 指定要处理的文件夹路径
folder_path = 'F:\Datasets_project\datasets/roof\labels'  # 替换为实际文件夹路径
import os

# 定义类别映射字典
class_mapping = {
    '0': '5'
}

# 遍历文件夹中的所有.txt标签文件
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        # 读取标签文件
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 替换类别编号并保留原始行数和列数
        updated_lines = []
        for line in lines:
            parts = line.split()
            if parts[0] in class_mapping:
                parts[0] = class_mapping[parts[0]]
            updated_line = " ".join(parts)
            updated_lines.append(updated_line)

        # 写入替换后的标签文件（保留原始行数和列数）
        with open(file_path, 'w') as file:
            for updated_line in updated_lines:
                file.write(updated_line + "\n")  # 添加换行符以保留原始行数和列数