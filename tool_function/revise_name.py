import os,sys,re                       #导入模块
def rename_files():             #定义函数名称
    old_names = os.listdir( path )  #取路径下的文件名，生成列表
    for old_name in old_names:      #遍历列表下的文件名
            if  old_name!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
               if old_name.endswith('.xml'):   #当文件名以.txt后缀结尾时
                    new_name=old_name.replace('old_names','roof_railing')   #将原来名字里的‘.txt’替换为‘-test.txt’,相当于加个后缀了
                    os.rename(os.path.join(path,old_name),os.path.join(path,new_name))  #重命名文件
                    print (old_name,"has been renamed successfully! New name is: ",new_name)  #输出提示

if __name__ == '__main__':
        path = r'F:\Datasets_project\datasets\glasswall\glasswall_original/labels_xml'   #运行程序前，记得修改主文件夹路径！
        rename_files()         #调用定义的函数，注意名称与定义的函数名一致