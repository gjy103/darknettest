import os
from os import listdir, getcwd
from os.path import join

# 在VOCdevkit 添加代码文件train&val.py。运行后自动划分图片为训练集和测试集写入之前手动创建的空train.txt,val.txt文件
if __name__ == '__main__':
    source_folder = r'D:\python WorkSpace\darknet\darknet-master\VOC2021\JPEGImages'#图片源目录
    dest = r'D:\python WorkSpace\darknet\darknet-master\VOC2021\ImageSets\Main\train.txt'  # train.txt文件路径
    dest2 = r'D:\python WorkSpace\darknet\darknet-master\VOC2021\ImageSets\Main\val.txt'  # val.txt文件路径
    dest3 = r'D:\python WorkSpace\darknet\darknet-master\VOC2021\ImageSets\Main\test.txt'  # test.txt文件路径
    file_list = os.listdir(source_folder)
    train_file = open(dest, 'a')
    val_file = open(dest2, 'a')
    test_file = open(dest3, 'a')
    file_num = 0
    for file_obj in file_list:
        file_path = os.path.join(source_folder, file_obj)
        file_name, file_extend = os.path.splitext(file_obj)
        file_num = file_num + 1

        if file_num % 4 == 0:  # 每隔4张选取一张验证集
        						#可自由选择训练集与测试集比例如果想设为9:1则把4改成9
            val_file.write(file_name + '\n')
        elif file_num % 4 == 1:
            train_file.write(file_name + '\n')
        else:
            test_file.write(file_name + '\n')


        # val_file.write(file_name + '\n')
        #
        # train_file.write(file_name + '\n')
train_file.close()
val_file.close()
test_file.close()