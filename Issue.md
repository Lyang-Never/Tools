## 1、onnx 、 TensorRT

版本问题
```
pytorch 1.1/1.2 对应 Tensorrt6.x
pytorch 1.6     对应 Tensorrt7.x

```
OP问题
```
ReLU6 不支持
PReLU    torch1.1/1.2转onnx的时候不支持    torch1.6是支持的
bn1d似乎有 unsqueeze 和squeeze操作  tensorrt6.x转的时候有问题

```
动态推理问题
```
一般不要这种reshape(x,-1) 或者 view(x,-1) 操作，可以用flatten来代替,注意torch1.1似乎没有nn.Flatten()这个块  torch1.6是有的

```
使用问题
```
Tensorrt 6.0  
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64
export LD_LIBRARY_PATH=/home/hbk/software/TensorRT-6.0.1.5/lib:$LD_LIBRARY_PATH
/home/hbk/software/TensorRT-6.0.1.5/bin/trtexec --onnx=torch1_1_flatten.onnx --verbose

Tensorrt 7.0
iec8:Su/TensorRT-7.0.0.11

# 半精度导出
 ./bin/trtexec --onnx=~.onnx --fp16 --saveEngine=~.engine 
# 全精度导出
./bin/trtexec --onnx=~.onnx --saveEngine=~.engine 

# 导出trt
./bin/trtexec --loadEngine=32.engine --exportOutput=~.trt 
```
