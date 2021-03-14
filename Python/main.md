## 1. 列表 元组 字典 字符串 ☃️


## 2. 函数 类 对象 ☃️


## 3.异常 ☃️


## 4. 方法 属性 迭代器 ☃️


## 5. 正则表达式 ☃️


## 6. 常用模块 ☃️


## 7. 文件和流 数据存储 ☃️


## 8. TCP UDP 网络高级编程 ☃️


## 9. 多线程 ☃️


## 10. GUI: tkinter Pyqt5 ☃️


### 10.2.1 label显示img
```
from PyQt5.Qt import QtGui

# 方法1
img_path="image_path.jpg"
pic_show_label = QtWidgets.QLabel()
pic_show_label.resize(500,500)

image = QtGui.QPixmap(img_path).scaled(400, 400)
pic_show_label.setPixmap(image)

# 方法2
pic_show_label = QtWidgets.QLabel()
pic_show_label.resize(500,500)
 

img_path="image_path.jpg"
img=cv2.imread(img_path)
# 通道转化
RGBImg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# 将图片转化成Qt可读格式
image=QtGui.QImage(RGBImg,RGBImg.shape[1],RGBImg.shape[0],QtGui.QImage.FormatRGB888)
 
image = QtGui.QPixmap(image).scaled(400, 400)
pic_show_label.setPixmap(image)
```
### 10.2.2 QT designer 转化为代码
```
QT designer所在位置：F:\python3.6.5\Lib\site-packages\qt5_applications\Qt\bin 
pyuic5 -o ui_test.py test.ui -x
```


## 11. Web: Flask Django ☃️


## 12. Numpy matplotlib pands ☃️


## 13. 爬虫 ☃️
