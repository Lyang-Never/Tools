## 1、pip

豆瓣：

```
pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com  some-package   
```

清华：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package 
```

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

