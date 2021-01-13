## 创建：
          conda create -n py3(name) python=3.5


## 激活：
          linux\osx : source activate  py3

          windows: activate py3

## 列出环境：
          conda env list  /  conda info -e

## 删除环境: 
          conda env remove -n py3

## 切换：
          source activate

## 退出：
          linux/osx:source deactivate py3
          windows: deactivate py3
          
          conda4: conda deavtivate py3
## 镜像&问题&解决：
          添加镜像：
          conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
          conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
          conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
          conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
          conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
          conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
          conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
          conda config --set show_channel_urls yes
          
          可以通过 vim ~/.condarc 查看（linux下）或者  conda config --show
          然后通过torch官网命令：
          eg：conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1   （去掉 -c pytorch）
          
          清华开源软件镜像地址：https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/linux-64/
          必须保证在这个镜像里面找到 相应版本的cudatoolkit 和 pytorch   （现在似乎只支持到torch1.5）
          （装其他版本可以试着把 https 换成 http ，试验了下似乎可以成功。）
          
          问题&解决：
          Conda - Downloaded bytes did not match Content-Length 问题  conda config --set remote_read_timeout_secs 600.0 解决   
          
