import os

path = 'F:\Datasets_project\datasets/trunk\images'
# path = 'C:/Users\Ticotico\Downloads/roof\labels'

names = os.listdir(path)  # 读取原文件名

len = len(names)  # 获取文件个数
num = [0] * len

# for i in range(int(len)):
#     print("%03d" % i)

for i in range(int(len)):
    num[i] = "%03d" % (i) # 三位数字编码  从000开始

    temp = names[i]
    new_name = 'trunk_' + num[i] + '.jpg'
    os.rename(path + '/' + temp, path + '/' + new_name)
