# Py :snowman:

## 1 xml文件处理和json文件处理

```python
# xml
import xml.etree.ElementTree as ET
    root = ET.parse(anno_path).getroot()
    size = root.find('size')
    width = float(size.find('width').text)
    height = float(size.find('height').text)
    for obj in root.iter('object'):
        xml_box = obj.find('bndbox')
        xmin = (float(xml_box.find('xmin').text) - 1)
        ymin = (float(xml_box.find('ymin').text) - 1)
        xmax = (float(xml_box.find('xmax').text) - 1)
        ymax = (float(xml_box.find('ymax').text) - 1)
        
# json

 dumps将一个字典转换成json
 dump 将一个文件转换成json
 loads 读取sring 转化成字典
 load 读取filename转化成字典
 
 with open(osp.join(save_path,'train.json'),'w') as f:
    json_str = json.dumps(coco_json,indent=1)
    f.write(json_str)
```

## 2 cv2 和 plt
  ```python
  resize: 
  cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
  cv2.putText(img, text, (40,60), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1, 4)
  
  cv2.rectangle(img, (240, 0), (480, 375), (0, 255, 0), 2)   # pt1和pt2需是int
  
  
  plt.show(numpy格式)
  
  
  
  # cv2 处理视频流
  '''
  保存avi视频流
  
  '''
  import cv2
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,400))   # width,height
  out.write(frame) #frame是单帧的img
  
  
  frame_width = video.get(3)  / video.get(cv2.CAP_PROP_FRAME_WIDTH)
  frame_height = video.get(4) / video.get(cv2.CAP_PROP_FRAME_HEIGHT)
   = video.get(7) /  video.get(cv2.CV_CAP_PROP_FRAME_COUNT)
  ```

## 3 常用的操作

```python
  random.sample(list,len)    #从list中随机取固定长度的list1
```


## 4 img读取操作

```python
 <1> img = cv2.imread('test.jpg')
     # BGR,.shape得到（H,W,C） np.ndarray
 <2> from PIL import Image
     Image = Image.open('test.jpg')
     # RGB, .size 得到(w,h)
 <3> import mxnet as mx
     mx_img = mx.image.imread('test.jpg')   # args：同下
     # RGB, .shape(H,W,C)
     
     img = mx.image.imdecode(open('test.jpg','rb').read())   # 数据流方式   args:flag = 1 / 0 (3channels/gray),to_rgb = 1 / 0 (RGB/BGR)
     
     # cv2 -> Image
     image1 = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))   # array
     # Image -> cv2
     img1 = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)    # RGB2BGR
     
     
```


## 5 二进制操作img
```
img_path = 'xx.jpg'
with open(img_path,'rb') as f:
  _b = f.read()
img = mx.image.imdecode(_b)
# img 是mx.nd.NDArray ，需要asnumpy 一下
```

## 6 pickle 用于序列化和反序列化Python对象结构的二进制协议
```
# 存储，可以将上述的_b存入一个.bin文件中
import pickle
with open('xx.bin','wb') as f:
  pickle.dump(_b,f,protocol=pickle.HIGHEST_PROTOCOL)
  
# 读取
with open('xx.bin','rb') as f:
  _b = pickle.load(f,encoding='iso-8859-1')

```

## 7 绘制间隔中心点
```

import numpy as np
import cv2

h,w = 200,200
img = np.random.randint(0,1,(h,w,3),dtype=np.int8)
cv2.imwrite('raw.jpg',img)

stride = [8,10,20]
sml_size = [(h/item,w/item) for item in stride]
colors = [(0,0,255),(0,255,0),(255,0,0),(255,255,0),(0,255,255),(255,0,255)]

for i,item in enumerate(stride):
    _h,_w = sml_size[i]
    shifts_x = np.arange(0,_w*item,_w,dtype=np.float32)
    shifts_y = np.arange(0,_h*item,_h,dtype=np.float32)

    shift_y,shift_x = np.meshgrid(shifts_y,shifts_x)
    shift_y = shift_y.reshape(-1)
    shift_x = shift_x.reshape(-1)
    coords = np.stack([shift_x,shift_y],-1)
    coords_center = coords + item//2
    for num in range(coords.shape[0]):
        cv2.circle(img,tuple(coords[num]),2,colors[i],-1)
        cv2.circle(img,tuple(coords_center[num]),1,colors[i+3],-1)
    cv2.imwrite('stride_%d.jpg'%(i),img)
cv2.imwrite('handle.jpg',img)


🔺cv2.circle(args) 中 center可以是float,但必须是tuple，list不行
🔺 np.arange，np.meshgrid， np.stack
```

# Pytorch :snowman:




# Mxnet :snowman:

## 1 rec文件处理（读 写）


