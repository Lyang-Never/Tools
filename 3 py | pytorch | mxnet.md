# Py :snowman:

## 1 xml文件处理和json文件处理


## 2 cv2 和 plt
  ```python
  resize: 
  
  plt.show(numpy格式)
  
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

# Pytorch :snowman:




# Mxnet :snowman:

## 1 rec文件处理（读 写）


