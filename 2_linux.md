## :alien: zip | rar |  tar
### zip
``` 
    解压
    unzip test.zip -d  +指定路径

    压缩
    zip file1.zip file1
    zip -r file1.zip file1 file2 dir1 将几个文件和目录同时压缩成一个zip格式的压缩包
```
### rar
```
  压缩
  rar a test.rar xx.txt yy.txt  ss
  (将yy.txt,xx.txt,ss文件夹压缩为test.rar)

  解压
  unrar e test.rar  /  rar e test.rar
  
```
### tar
```
  解压
  tar -xvf xxx.tar 释放一个包
  tar -xvf aaa.tar -C /tmp 将压缩包释放到 /tmp目录下 
  压缩
  tar -cvf xxx.tar file1 创建一个非压缩的 tarball 
  tar -cvf xxx.tar file1 file2 dir1  将多个文件打包

```

### tar.gz
```
  解压
  tar -zxvf archive.tar.gz 
  压缩
  tar -cvfz archive.tar.gz dir1 

```


### 查看文件大小
```
du -lh max-depth=1
```
