## 二进制操作img
```
img_path = 'xx.jpg'
with open(img_path,'rb') as f:
  _b = f.read()
img = mx.image.imdecode(_b)
# img 是mx.nd.NDArray ，需要asnumpy 一下
```

## pickle 用于序列化和反序列化Python对象结构的二进制协议
```
# 存储，可以将上述的_b存入一个.bin文件中
import pickle
with open('xx.bin','wb') as f:
  pickle.dump(_b,f,protocol=pickle.HIGHEST_PROTOCOL)
  
# 读取
with open('xx.bin','rb') as f:
  _b = pickle.load(f,encoding='iso-8859-1')

```
