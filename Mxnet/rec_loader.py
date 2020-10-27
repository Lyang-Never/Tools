```
.rec\.idx 的获得：
step1：python incubator-mxnet\tools\im2rec.py data/train data/train  --list --recursive     第一个data/train代表.lst生成的位置和名称，即data下train.lst，第二个data/train 代表img所在路径
step2: python incubator-mxnet\tools\im2rec.py data/train.lst data/train    后面这个data/train代表img所在路径

```


import cv2
import mxnet as mx

_rec = './data/train.rec'
_idx = './data/train.idx'
Label = []

data_rec = mx.recordio.MXIndexedRecordIO(_idx,_rec,'r')

for i in range(len(data_rec.keys)):
    s = data_rec.read_idx(i)
    header,img = mx.recordio.unpack(s)
    Label.append(header.label)
    if len(img)>0:
        img = mx.image.imdecode(img,flag=1,to_rgb=0).asnumpy()
        # img = mx.image.imdecode(img).asnumpy()[:,:,::-1]
        cv2.imwrite('./data/%d.jpg'%i,img)
        
print(Label)

