## label显示img
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
pic_show_label.setPixmap(image
```
