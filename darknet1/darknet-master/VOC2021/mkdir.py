import os
import time

def mkFolder(path):
    year = str(time.localtime()[0])
    floderName = 'VOC' + year#生成主文件夹的名称，比如今年是2021，则主文件夹的名称为VOC2021
    # path = os.path.normpath(path)
    floderPath = os.path.join(path, floderName)
    if not os.path.exists(floderPath):
        os.makedirs(floderPath)
    print(floderPath)
    subfloderName = ['Annotations', 'ImageSets', 'JPEGImages', 'labels', 'TESTImages']#生成的子文件夹名称
    for name in subfloderName:
        subfloderPath = os.path.join(path, floderName, name)
        print(subfloderPath)
        if not os.path.exists(subfloderPath):
            os.makedirs(subfloderPath)
        if name == 'ImageSets':
            secSubFolderName = 'Main'
            secSubFolderPath = os.path.join(path, floderName, name, secSubFolderName)
            print(secSubFolderPath)
            if not os.path.exists(secSubFolderPath):
                os.makedirs(secSubFolderPath)


if __name__ == '__main__':
    path = r'D:\python WorkSpace\darknet\darknet-master'  #更换为自己的文件夹路径
    mkFolder(path)